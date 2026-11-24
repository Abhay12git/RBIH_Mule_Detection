from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

try:
    import networkx as nx
except ImportError:
    nx = None

try:
    import duckdb
except ImportError:
    duckdb = None


# =============================================================================
# RBIH Mule Detection — Interactive Research Workbench
#
# Safety model:
# - No work starts automatically when the app opens.
# - Training/evaluation scripts must be explicitly allowlisted in
#   dashboard_config.json by the repository owner.
# - Scripts are executed as argument lists (never through shell=True).
# - No arbitrary shell/terminal input is accepted from the UI.
# - Graph/data views load bounded samples only.
# - The app does not alter source code, raw data, or existing model artifacts.
# =============================================================================

st.set_page_config(
    page_title="RBIH Mule Detection | Research Workbench",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
DOCS = ROOT / "docs"
CONFIGS = ROOT / "configs"
SRC = ROOT / "src"
DASHBOARD_CONFIG = ROOT / "dashboard_config.json"
RUN_LOG = RESULTS / "dashboard_experiment_log.csv"

DEFAULT_CONFIG = {
    "approved_scripts": [],
    "graph_data_paths": [],
    "max_graph_rows": 5000,
    "max_graph_nodes": 250,
    "experiment_timeout_seconds": 1800,
}

st.sidebar.title("RBIH Mule Detection")
st.sidebar.caption("Interactive Research & Engineering Workbench")
st.sidebar.markdown("**Application:** V2 · Interactive")
st.sidebar.markdown("**Mode:** Local repository")
st.sidebar.info(
    "The app is read-only with respect to source datasets and model artifacts. "
    "It writes only its own experiment log and explicitly launched script outputs."
)


def ensure_dirs() -> None:
    RESULTS.mkdir(exist_ok=True)


def load_config() -> dict[str, Any]:
    if not DASHBOARD_CONFIG.exists():
        DASHBOARD_CONFIG.write_text(
            json.dumps(DEFAULT_CONFIG, indent=2), encoding="utf-8"
        )
        return DEFAULT_CONFIG.copy()
    try:
        loaded = json.loads(DASHBOARD_CONFIG.read_text(encoding="utf-8"))
        merged = DEFAULT_CONFIG.copy()
        merged.update(loaded if isinstance(loaded, dict) else {})
        if not isinstance(merged.get("approved_scripts"), list):
            merged["approved_scripts"] = []
        if not isinstance(merged.get("graph_data_paths"), list):
            merged["graph_data_paths"] = []
        return merged
    except Exception as exc:
        st.error(f"Could not parse dashboard_config.json: {exc}")
        return DEFAULT_CONFIG.copy()


CFG = load_config()


def safe_repo_path(value: str) -> Path | None:
    """Resolve a repository-relative path and reject path traversal."""
    try:
        candidate = (ROOT / value).resolve()
        candidate.relative_to(ROOT.resolve())
        return candidate
    except Exception:
        return None


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_csv(path: Path, nrows: int | None = None) -> pd.DataFrame | None:
    try:
        return pd.read_csv(path, nrows=nrows)
    except Exception as exc:
        st.error(f"Could not read {rel(path)}: {exc}")
        return None


def read_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        st.error(f"Could not read {rel(path)}: {exc}")
        return None


def read_bounded_table(path: Path, limit: int) -> pd.DataFrame:
    """Read a bounded CSV/Parquet sample. Never scans the raw transaction folder."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path, nrows=limit, low_memory=False)
    if suffix in {".parquet", ".pq"}:
        if duckdb is not None:
            con = duckdb.connect(database=":memory:")
            try:
                # Path is escaped as a SQL string literal.
                escaped = str(path).replace("'", "''")
                return con.execute(
                    f"SELECT * FROM read_parquet('{escaped}') LIMIT {int(limit)}"
                ).df()
            finally:
                con.close()
        # Fallback is acceptable only for files that fit in memory.
        return pd.read_parquet(path).head(limit)
    raise ValueError(f"Unsupported table type: {suffix}")


def normalise(value: str) -> str:
    return "".join(ch.lower() for ch in str(value) if ch.isalnum())


def find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    by_norm = {normalise(c): c for c in df.columns}
    for candidate in candidates:
        if normalise(candidate) in by_norm:
            return by_norm[normalise(candidate)]
    for candidate in candidates:
        key = normalise(candidate)
        for norm_name, original in by_norm.items():
            if key and (key in norm_name or norm_name in key):
                return original
    return None


def discover_comparison() -> tuple[Path | None, pd.DataFrame | None]:
    candidates = [
        RESULTS / "model_comparison.csv",
        RESULTS / "model_comparison_metrics.csv",
        RESULTS / "comparison.csv",
    ]
    for path in candidates:
        if path.exists():
            return path, read_csv(path)
    return None, None


def discover_graph_files() -> list[Path]:
    # Deliberately exclude data/raw: raw transaction tables can be enormous and
    # are not needed for interactive exploration.
    search_dirs = [
        ROOT / "data" / "graph",
        ROOT / "data" / "processed",
        ROOT / "data" / "interim",
        ROOT / "data" / "features",
        RESULTS,
    ]
    found: set[Path] = set()
    configured = CFG.get("graph_data_paths", [])
    for item in configured:
        p = safe_repo_path(str(item))
        if p and p.is_file() and p.suffix.lower() in {".csv", ".parquet", ".pq"}:
            found.add(p)
    for directory in search_dirs:
        if directory.exists():
            for p in directory.rglob("*"):
                if p.is_file() and p.suffix.lower() in {".csv", ".parquet", ".pq"}:
                    name = p.name.lower()
                    if any(token in name for token in ("edge", "graph", "counterpart", "community", "node")):
                        found.add(p)
    return sorted(found)


def discover_scripts() -> list[Path]:
    if not SRC.exists():
        return []
    candidates = []
    for p in SRC.rglob("*.py"):
        low = p.name.lower()
        if any(token in low for token in ("train", "evaluate", "experiment", "ablation")):
            candidates.append(p)
    return sorted(candidates)


def approved_script_entries() -> list[dict[str, Any]]:
    entries = []
    for item in CFG.get("approved_scripts", []):
        if isinstance(item, str):
            entries.append({"path": item, "args": []})
        elif isinstance(item, dict) and item.get("path"):
            entries.append({"path": str(item["path"]), "args": item.get("args", [])})
    return entries


def load_run_log() -> pd.DataFrame:
    if RUN_LOG.exists():
        df = read_csv(RUN_LOG)
        if df is not None:
            return df
    return pd.DataFrame(columns=[
        "run_id", "started_at_utc", "script", "args", "status",
        "duration_seconds", "return_code", "notes"
    ])


def append_run_log(row: dict[str, Any]) -> None:
    ensure_dirs()
    log = load_run_log()
    log = pd.concat([log, pd.DataFrame([row])], ignore_index=True)
    log.to_csv(RUN_LOG, index=False)


def discover_importance() -> tuple[Path | None, pd.DataFrame | None]:
    for path in [
        RESULTS / "lightgbm_graph_extended_feature_importance.csv",
        RESULTS / "feature_importance.csv",
    ]:
        if path.exists():
            return path, read_csv(path)
    return None, None


def show_metric_jsons() -> None:
    jsons = sorted(set(RESULTS.glob("*metric*.json")) | set(RESULTS.glob("*metrics*.json")))
    if not jsons:
        st.info("No metric JSON artifacts found under results/.")
        return
    selected = st.selectbox(
        "Metric artifact",
        jsons,
        format_func=rel,
        key="metric_artifact_select",
    )
    payload = read_json(selected)
    if payload is not None:
        st.caption(f"Source: `{rel(selected)}`")
        st.json(payload)


# Header
st.title("🔎 RBIH Mule Detection")
st.subheader("Interactive Research & Engineering Workbench")
st.caption(
    "Local interactive UI for experiment evidence, graph exploration, "
    "explainability, controlled experiment execution, and research planning."
)

comparison_path, comparison_df = discover_comparison()
importance_path, importance_df = discover_importance()
graph_files = discover_graph_files()
script_candidates = discover_scripts()
approved_scripts = approved_script_entries()

pages = st.tabs([
    "Overview",
    "Experiments",
    "Graph explorer",
    "Explainability",
    "Temporal lab",
    "Audit & roadmap",
    "Run manager",
])

# =============================================================================
# OVERVIEW
# =============================================================================
with pages[0]:
    st.header("Project status")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Comparison artifact", "Available" if comparison_df is not None else "Missing")
    c2.metric("Graph data files", len(graph_files))
    c3.metric("Importance artifact", "Available" if importance_df is not None else "Missing")
    c4.metric("Approved experiment scripts", len(approved_scripts))

    st.warning(
        "Evidence is not the same as reproduction. Existing metric files are shown "
        "as repository-reported results; this app does not certify that they can be reproduced."
    )

    st.markdown("### Experiment comparison")
    if comparison_df is not None:
        st.caption(f"Source: `{rel(comparison_path)}`")
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    else:
        st.info("No standard model comparison CSV found. See the Experiments tab to inspect other metric artifacts.")

    st.markdown("### Available local assets")
    asset_table = pd.DataFrame([
        {"Asset": "Results JSON files", "Count": len(list(RESULTS.glob("*.json"))) if RESULTS.exists() else 0},
        {"Asset": "Results CSV files", "Count": len(list(RESULTS.glob("*.csv"))) if RESULTS.exists() else 0},
        {"Asset": "Graph candidate files (non-raw)", "Count": len(graph_files)},
        {"Asset": "Candidate training/evaluation scripts", "Count": len(script_candidates)},
        {"Asset": "Approved scripts for UI execution", "Count": len(approved_scripts)},
    ])
    st.dataframe(asset_table, use_container_width=True, hide_index=True)

    st.markdown("### Research status")
    st.markdown(
        "- **Phase 0:** repository audit prepared from inspected source snapshot.\n"
        "- **Phase 1:** baseline reproduction, environment pinning, tests, and shared encoders remain to be completed.\n"
        "- **Phase 2:** graph feature semantics and controlled ablations remain to be completed.\n"
        "- **Phase 3:** point-in-time graph construction and chronological evaluation remain to be implemented.\n"
        "- **Phase 4:** production readiness, explainability validation, and monitoring remain future work."
    )

# =============================================================================
# EXPERIMENTS
# =============================================================================
with pages[1]:
    st.header("Experiment comparison")
    if comparison_df is None:
        st.info("No recognised model comparison CSV found under results/.")
    else:
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
        model_col = find_column(comparison_df, ["model", "experiment", "model_name", "experiment_id", "name"])
        metric_candidates = {
            "ROC-AUC": ["roc_auc", "roc_auc_score", "rocauc", "auc"],
            "PR-AUC": ["pr_auc", "pr_auc_score", "average_precision", "prauc"],
            "Recall": ["recall", "recall_score"],
            "Precision": ["precision", "precision_score"],
            "F1": ["f1", "f1_score"],
        }
        available = {k: find_column(comparison_df, v) for k, v in metric_candidates.items()}
        available = {k: v for k, v in available.items() if v}
        if model_col and available:
            metric = st.selectbox("Visualise metric", list(available), key="comparison_metric")
            metric_col = available[metric]
            plot_df = comparison_df[[model_col, metric_col]].copy()
            plot_df[metric_col] = pd.to_numeric(plot_df[metric_col], errors="coerce")
            plot_df = plot_df.dropna(subset=[metric_col])
            if not plot_df.empty:
                st.plotly_chart(
                    px.bar(plot_df, x=model_col, y=metric_col, text_auto=".4f", title=f"{metric} by model"),
                    use_container_width=True,
                )
        else:
            st.caption("Automatic charting needs recognisable model and metric columns.")

    st.markdown("### Result JSON files")
    show_metric_jsons()

    st.markdown("### Experiment history created by this dashboard")
    run_log = load_run_log()
    if run_log.empty:
        st.info("No experiments have been launched through this dashboard yet.")
    else:
        st.dataframe(run_log.sort_values("started_at_utc", ascending=False), use_container_width=True, hide_index=True)

# =============================================================================
# GRAPH EXPLORER
# =============================================================================
with pages[2]:
    st.header("Graph explorer")
    st.write(
        "Choose an existing graph/edge table to inspect a bounded sample. "
        "Raw transaction directories are intentionally excluded."
    )
    if nx is None:
        st.error("NetworkX is not installed. Install the repository graph dependencies or add `networkx`.")
    elif not graph_files:
        st.info(
            "No graph/edge CSV or Parquet files were discovered in data/graph, data/processed, "
            "data/interim, data/features, or results. If your graph file is elsewhere, add its "
            "repository-relative path to `graph_data_paths` in dashboard_config.json."
        )
    else:
        chosen_graph = st.selectbox("Graph data file", graph_files, format_func=rel)
        max_rows = int(CFG.get("max_graph_rows", 5000))
        max_rows = max(100, min(max_rows, 50000))
        st.caption(f"Loading at most {max_rows:,} rows from this file.")
        try:
            graph_df = read_bounded_table(chosen_graph, max_rows)
            st.write(f"Loaded sample: **{len(graph_df):,} rows**, {len(graph_df.columns)} columns.")
            st.dataframe(graph_df.head(100), use_container_width=True, hide_index=True)
            source_col = find_column(graph_df, ["source", "source_account", "account_id", "src", "from_account"])
            target_col = find_column(graph_df, ["target", "counterparty_id", "destination", "dst", "to_account"])
            if source_col and target_col:
                columns = list(graph_df.columns)
                source_col = st.selectbox("Source / origin column", columns, index=columns.index(source_col))
                target_col = st.selectbox("Target / destination column", columns, index=columns.index(target_col))
                weight_guess = find_column(graph_df, ["weight", "transaction_count", "count", "total_amount", "volume"])
                weight_col = st.selectbox(
                    "Optional edge weight column",
                    ["(unweighted)"] + columns,
                    index=(columns.index(weight_guess) + 1) if weight_guess else 0,
                )
                max_nodes = int(CFG.get("max_graph_nodes", 250))
                max_nodes = max(20, min(max_nodes, 500))
                working = graph_df[[source_col, target_col] + ([] if weight_col == "(unweighted)" else [weight_col])].copy()
                working = working.dropna(subset=[source_col, target_col])
                working[source_col] = working[source_col].astype(str)
                working[target_col] = working[target_col].astype(str)
                working = working[working[source_col] != working[target_col]]
                account_options = sorted(set(working[source_col]) | set(working[target_col]))
                if account_options:
                    selected_account = st.selectbox("Inspect account / node", account_options)
                    outgoing = working[working[source_col] == selected_account]
                    incoming = working[working[target_col] == selected_account]
                    n1, n2, n3 = st.columns(3)
                    n1.metric("Outgoing edges", len(outgoing))
                    n2.metric("Incoming edges", len(incoming))
                    n3.metric("Unique neighbours", len(set(outgoing[target_col]) | set(incoming[source_col])))
                    st.markdown("#### Account relationships")
                    left, right = st.columns(2)
                    with left:
                        st.markdown("**Outgoing counterparties**")
                        st.dataframe(outgoing.head(100), use_container_width=True, hide_index=True)
                    with right:
                        st.markdown("**Incoming counterparties**")
                        st.dataframe(incoming.head(100), use_container_width=True, hide_index=True)

                    # Build a small local neighbourhood for a responsive plot.
                    local_edges = pd.concat([outgoing, incoming], ignore_index=True).drop_duplicates()
                    nodes = set(local_edges[source_col]) | set(local_edges[target_col])
                    if len(nodes) > max_nodes:
                        # Keep the selected node and the highest-degree neighbours.
                        degree = pd.concat([local_edges[source_col], local_edges[target_col]]).value_counts()
                        keep = set(degree.head(max_nodes).index) | {selected_account}
                        local_edges = local_edges[
                            local_edges[source_col].isin(keep) & local_edges[target_col].isin(keep)
                        ]
                        nodes = set(local_edges[source_col]) | set(local_edges[target_col])
                    if len(nodes) >= 2 and len(local_edges) > 0:
                        graph = nx.DiGraph()
                        for _, row in local_edges.iterrows():
                            weight = 1.0
                            if weight_col != "(unweighted)":
                                try:
                                    weight = float(row[weight_col])
                                except (TypeError, ValueError):
                                    weight = 1.0
                            graph.add_edge(row[source_col], row[target_col], weight=weight)
                        positions = nx.spring_layout(graph, seed=42, k=None)
                        edge_x, edge_y = [], []
                        for u, v in graph.edges():
                            x0, y0 = positions[u]
                            x1, y1 = positions[v]
                            edge_x.extend([x0, x1, None])
                            edge_y.extend([y0, y1, None])
                        node_x = [positions[n][0] for n in graph.nodes()]
                        node_y = [positions[n][1] for n in graph.nodes()]
                        node_text = [
                            f"Account: {n}<br>In-degree: {graph.in_degree(n)}<br>Out-degree: {graph.out_degree(n)}"
                            for n in graph.nodes()
                        ]
                        node_size = [20 if n == selected_account else 10 for n in graph.nodes()]
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(
                            x=edge_x, y=edge_y, mode="lines",
                            line=dict(width=1), hoverinfo="none", name="Directed edges"
                        ))
                        fig.add_trace(go.Scatter(
                            x=node_x, y=node_y, mode="markers+text",
                            text=[n if n == selected_account else "" for n in graph.nodes()],
                            textposition="top center",
                            marker=dict(size=node_size, line=dict(width=1)),
                            hovertext=node_text, hoverinfo="text", name="Accounts"
                        ))
                        fig.update_layout(
                            title="Local directed transaction network",
                            showlegend=False, height=600,
                            xaxis=dict(visible=False), yaxis=dict(visible=False),
                            margin=dict(l=10, r=10, t=50, b=10),
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.caption("Network layout is a visual aid; edge direction follows the selected source → target columns.")
            else:
                st.warning("Could not infer source and target columns. Inspect the table above and select a suitable edge file.")
        except Exception as exc:
            st.error(f"Graph file could not be explored: {exc}")

# =============================================================================
# EXPLAINABILITY
# =============================================================================
with pages[3]:
    st.header("Explainability lab")
    st.write("Recorded feature importance and SHAP artifacts are handled as separate evidence types.")
    if importance_df is not None:
        st.caption(f"Feature importance source: `{rel(importance_path)}`")
        st.dataframe(importance_df, use_container_width=True, hide_index=True)
        fcol = find_column(importance_df, ["feature", "feature_name", "name"])
        vcol = find_column(importance_df, ["importance", "gain", "split", "weight", "value"])
        if fcol and vcol:
            chart_df = importance_df[[fcol, vcol]].copy()
            chart_df[vcol] = pd.to_numeric(chart_df[vcol], errors="coerce")
            chart_df = chart_df.dropna().nlargest(30, vcol).sort_values(vcol)
            if not chart_df.empty:
                st.plotly_chart(
                    px.bar(chart_df, x=vcol, y=fcol, orientation="h", title="Top 30 recorded feature importance values"),
                    use_container_width=True,
                )
    else:
        st.info("No recognised feature-importance CSV found.")

    shap_images = []
    if RESULTS.exists():
        for pattern in ("*shap*.png", "*shap*.jpg", "*shap*.jpeg"):
            shap_images.extend(RESULTS.glob(pattern))
    if shap_images:
        st.markdown("### SHAP artifacts")
        for start in range(0, len(shap_images), 2):
            cols = st.columns(2)
            for idx, image_path in enumerate(shap_images[start:start + 2]):
                cols[idx].image(str(image_path), caption=rel(image_path), use_container_width=True)
    else:
        st.info("No SHAP image artifacts found under results/.")

    st.warning(
        "The audited graph-vs-tabular importance calculation is a share of recorded "
        "feature-importance values, not a SHAP attribution. Account-level explanations "
        "require a compatible saved model, feature row, and explainer; this UI does not fabricate them."
    )
    report = DOCS / "reports" / "explainability_report.md"
    if report.exists():
        with st.expander("Read explainability report"):
            st.markdown(report.read_text(encoding="utf-8"))

# =============================================================================
# TEMPORAL LAB
# =============================================================================
with pages[4]:
    st.header("Temporal leakage research lab")
    st.warning(
        "This page is a planning and metadata inspection tool. Selecting a cutoff does not "
        "rebuild graph features or run a temporal evaluation."
    )
    cutoff = st.date_input("Proposed prediction-time cutoff", value=pd.Timestamp("2025-01-01").date())
    st.info(f"Selected conceptual cutoff: **{cutoff.isoformat()}**")
    checks = [
        "Prediction timestamp and target horizon are defined.",
        "Transaction edges are filtered to transactions available at prediction time.",
        "Mutable account attributes are represented as-of the prediction timestamp.",
        "The semantics and observation time of mule_flag_date are confirmed.",
        "Categorical encoders and preprocessing are fitted on training data only.",
        "Community detection and graph aggregates cannot see future transactions.",
        "Frozen split IDs and cutoff are recorded in experiment metadata.",
        "Evaluation is performed on a genuinely later time period.",
        "Unseen-account and new-counterparty behaviour is specified.",
    ]
    st.markdown("### Temporal validity checklist")
    for i, item in enumerate(checks):
        st.checkbox(item, key=f"temporal_check_{i}")
    st.markdown("### Known questions from repository inspection")
    st.markdown(
        "- Transaction metadata contains `transaction_timestamp`.\n"
        "- Label schema contains `mule_flag_date`, but its precise semantics need confirmation.\n"
        "- Account status and freeze/unfreeze dates exist, but a status observation timestamp was not established.\n"
        "- The documented split is stratified 70/15/15; a chronological split was not found in the inspected documentation."
    )

# =============================================================================
# AUDIT & ROADMAP
# =============================================================================
with pages[5]:
    st.header("Audit & implementation roadmap")
    audit_path = DOCS / "implementation_audit.md"
    if audit_path.exists():
        st.markdown(audit_path.read_text(encoding="utf-8"))
    else:
        st.info("Copy the separately prepared implementation audit into docs/implementation_audit.md to show the full audit here.")
    st.markdown("### Key findings from the inspected repository snapshot")
    findings = [
        ("Category encoding", "Train/validation/test preparation independently creates category codes; mappings may not align."),
        ("Temporal cutoff", "Graph aggregation uses available transaction history without a point-in-time cutoff."),
        ("Community features", "Community aggregates are built before frozen split separation; controlled leakage evaluation is required."),
        ("Graph semantics", "Directed and undirected graph representations coexist; feature definitions need explicit contracts."),
        ("Baseline reproducibility", "Original E4B training source was not located; a later evaluation script uses different LightGBM settings."),
        ("GNN reproducibility", "GNN metric artifacts exist, but corresponding training source files were not found in the inspected tree."),
        ("Importance terminology", "Graph-vs-tabular importance is recorded model importance, not SHAP."),
        ("Tests", "No dedicated tests directory was present in the inspected snapshot."),
    ]
    st.dataframe(pd.DataFrame(findings, columns=["Area", "Observation"]), use_container_width=True, hide_index=True)

    roadmap = pd.DataFrame([
        ["Phase 0 — Reconnaissance", "Audit prepared", "Inspect source, map pipeline, verify hypotheses, record gaps."],
        ["Phase 1 — Reproducibility", "Planned", "Document environment, reproduce baseline, add tests, centralise encoders/config."],
        ["Phase 2 — Graph engineering", "Planned", "Clarify graph semantics, safe feature construction, controlled ablations."],
        ["Phase 3 — Temporal evaluation", "Planned", "Point-in-time graph construction and chronological evaluation."],
        ["Phase 4 — Production readiness", "Planned", "Explainability validation, monitoring, performance and operational docs."],
    ], columns=["Phase", "Status", "Scope"])
    st.markdown("### Roadmap")
    st.dataframe(roadmap, use_container_width=True, hide_index=True)

# =============================================================================
# RUN MANAGER
# =============================================================================
with pages[6]:
    st.header("Experiment run manager")
    st.write(
        "Launch a repository script only after you have reviewed it and explicitly "
        "allowlisted it in `dashboard_config.json`. This prevents accidental execution "
        "of arbitrary code from the UI."
    )

    st.markdown("### 1. Candidate scripts (not automatically executable)")
    if script_candidates:
        st.dataframe(
            pd.DataFrame([{"Script": rel(p), "Approved": any(e["path"] == rel(p) for e in approved_scripts)} for p in script_candidates]),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No candidate training/evaluation scripts discovered under src/.")

    st.markdown("### 2. Configure the allowlist")
    st.code(
        json.dumps({
            "approved_scripts": [
                {
                    "path": "src/evaluation/YOUR_REVIEWED_SCRIPT.py",
                    "args": []
                }
            ],
            "graph_data_paths": [],
            "max_graph_rows": 5000,
            "max_graph_nodes": 250,
            "experiment_timeout_seconds": 1800
        }, indent=2),
        language="json",
    )
    st.caption(
        "Edit dashboard_config.json manually. Add only scripts you have read and "
        "understand. Arguments are passed as a list, never as a shell command."
    )

    st.markdown("### 3. Launch an approved experiment")
    valid_entries = []
    for entry in approved_scripts:
        p = safe_repo_path(entry["path"])
        if p and p.is_file() and p.suffix == ".py":
            valid_entries.append((entry, p))

    if not valid_entries:
        st.info("No valid scripts are approved yet. Review a script, add it to dashboard_config.json, and restart the app.")
    else:
        labels = [f"{rel(path)} | args={entry.get('args', [])}" for entry, path in valid_entries]
        selection = st.selectbox("Approved script", range(len(labels)), format_func=lambda i: labels[i])
        selected_entry, selected_path = valid_entries[selection]
        st.code(selected_path.read_text(encoding="utf-8")[:12000], language="python")
        st.caption("Preview is limited to the first 12,000 characters. Read the full script before approving it.")
        timeout_seconds = int(CFG.get("experiment_timeout_seconds", 1800))
        timeout_seconds = max(30, min(timeout_seconds, 24 * 60 * 60))
        st.write(f"Configured timeout: **{timeout_seconds} seconds**")
        st.error(
            "Running this script may consume substantial CPU/GPU, read datasets, "
            "write model artifacts, or overwrite files depending on its implementation."
        )
        confirm = st.checkbox(
            f"I reviewed `{rel(selected_path)}` and explicitly approve executing it.",
            key="confirm_run_script",
        )
        if st.button("▶ Run approved experiment", type="primary", disabled=not confirm):
            started = datetime.now(timezone.utc)
            run_id = started.strftime("%Y%m%dT%H%M%SZ")
            args = selected_entry.get("args", [])
            if not isinstance(args, list) or not all(isinstance(x, (str, int, float)) for x in args):
                st.error("Configured args must be a JSON list of strings/numbers.")
            else:
                command = [sys.executable, str(selected_path)] + [str(x) for x in args]
                stdout_text = ""
                stderr_text = ""
                return_code = None
                status = "failed"
                with st.status(f"Running {rel(selected_path)} …", expanded=True) as status_box:
                    st.write("Command (no shell):")
                    st.code(" ".join([sys.executable, rel(selected_path)] + [str(x) for x in args]))
                    try:
                        result = subprocess.run(
                            command,
                            cwd=str(ROOT),
                            capture_output=True,
                            text=True,
                            timeout=timeout_seconds,
                            check=False,
                            env=os.environ.copy(),
                        )
                        stdout_text = result.stdout or ""
                        stderr_text = result.stderr or ""
                        return_code = result.returncode
                        status = "completed" if return_code == 0 else "failed"
                        status_box.update(
                            label=f"Experiment {status} (exit code {return_code})",
                            state="complete" if return_code == 0 else "error",
                        )
                    except subprocess.TimeoutExpired as exc:
                        stdout_text = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
                        stderr_text = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
                        stderr_text += f"\nTimed out after {timeout_seconds} seconds."
                        status = "timeout"
                        status_box.update(label="Experiment timed out", state="error")
                    except Exception as exc:
                        stderr_text = repr(exc)
                        status = "failed"
                        status_box.update(label="Experiment failed to start", state="error")

                duration = (datetime.now(timezone.utc) - started).total_seconds()
                append_run_log({
                    "run_id": run_id,
                    "started_at_utc": started.isoformat(),
                    "script": rel(selected_path),
                    "args": json.dumps(args),
                    "status": status,
                    "duration_seconds": round(duration, 2),
                    "return_code": return_code,
                    "notes": "",
                })
                st.metric("Duration (seconds)", f"{duration:.1f}")
                if stdout_text:
                    with st.expander("Standard output", expanded=True):
                        st.code(stdout_text[-30000:])
                if stderr_text:
                    with st.expander("Standard error", expanded=bool(status != "completed")):
                        st.code(stderr_text[-30000:])
                st.info("Run metadata was appended to results/dashboard_experiment_log.csv.")

    st.markdown("### Run history")
    history = load_run_log()
    if history.empty:
        st.info("No runs recorded yet.")
    else:
        st.dataframe(history.sort_values("started_at_utc", ascending=False), use_container_width=True, hide_index=True)

st.markdown("---")
st.caption(
    "RBIH Mule Detection Research Workbench · Local-only Streamlit app · "
    "No automatic training · No arbitrary shell execution · No raw transaction loading."
)
