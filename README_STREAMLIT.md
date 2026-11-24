# RBIH Mule Detection — Interactive Streamlit Workbench

## Install in your existing repository environment

Copy `app.py`, `dashboard_config.json`, and `requirements-dashboard.txt` into the **repository root** (beside README.md). Then run:

```bash
pip install -r requirements-dashboard.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (normally http://localhost:8501).

## Included functionality

- Overview of repository artifacts and experiment status.
- Model comparison charts from existing result CSVs and JSON metrics.
- Graph explorer for bounded samples of edge/graph CSV or Parquet files. It excludes `data/raw` intentionally.
- Account neighbourhood inspection with incoming/outgoing edges and a directed network plot.
- Feature-importance charts and existing SHAP image display.
- Temporal validity checklist (planning only; it does not yet rebuild temporal features).
- Audit findings and Phase 0–4 roadmap.
- Run manager for reviewed and explicitly allowlisted Python experiment scripts.

## Enable experiment execution safely

The run manager does **not** execute every discovered script. First inspect the entire script and its side effects. Then add it to `dashboard_config.json`:

```json
{
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
}
```

Restart Streamlit. The UI still requires a confirmation checkbox and a button click. The script is launched with the current Python interpreter, repository root as working directory, and `shell=False` (the default). It may nevertheless read data, consume CPU/GPU, or write/overwrite artifacts according to its own code. Do not approve a script until you have reviewed those effects.

## Configure graph data

The app automatically searches these locations for filenames containing terms such as `edge`, `graph`, `counterpart`, `community`, or `node`:

- `data/graph/`
- `data/processed/`
- `data/interim/`
- `data/features/`
- `results/`

It intentionally does not search `data/raw/`. If a graph table lives elsewhere inside the repository, add its relative path to `graph_data_paths` in `dashboard_config.json`, for example `data/derived/my_graph_edges.parquet`.

The app loads a bounded sample. For Parquet, DuckDB is used to apply `LIMIT` without reading the entire file into pandas. CSV is read with `nrows`.

## Important research limitations

- Metrics are displayed from existing repository artifacts; the app does not independently reproduce them.
- The temporal cutoff page is a checklist only. It does not filter transactions or rebuild point-in-time graph features.
- Account-level SHAP explanations require a compatible saved model, feature row, and explainer; no explanations are fabricated when these are absent.
- Graph explorer results are based on the selected bounded sample, not necessarily the complete graph.
- Run history is stored in `results/dashboard_experiment_log.csv`.
- The app does not change source code, raw datasets, or upstream Git state.

## Troubleshooting

- If a package is missing: rerun `pip install -r requirements-dashboard.txt` in the active environment.
- If the graph explorer finds no files: confirm your generated graph edge artifact exists, then add its relative path to `graph_data_paths`.
- If no experiment can be launched: review a training/evaluation script and explicitly add it to `approved_scripts`.
- If Streamlit reports an address in use: run `streamlit run app.py --server.port 8502`.
