# Client Applicability of the Mule Account Detection Framework

## Applying Behavioural and Graph Analytics for Future Financial Crime Detection

---

# Executive Summary

The mule account detection framework developed in this project demonstrates how a combination of behavioural analytics, graph intelligence, and machine learning can be deployed to identify high-risk accounts within large-scale transaction ecosystems.

The project achieved:

```text
ROC-AUC   = 0.9419

PR-AUC    = 0.7151

Precision = 0.7584

Recall    = 0.7602

F1        = 0.7593
```

on 28,828 completely unseen labelled accounts.

Beyond the model performance, the implementation provides a practical blueprint that financial institutions can use to operationalise fraud detection on future transaction data.

---

# Client Problem

Financial institutions continue to face increasing challenges related to:

- Mule Account Networks
- Money Laundering
- Rapid Money Movement
- Fraud Rings
- Payment Abuse
- Transaction Layering

Traditional transaction monitoring systems frequently generate large volumes of alerts while failing to identify sophisticated behavioural and network-level patterns.

Common limitations include:

```text
Rule-based systems

Static thresholds

Lack of behavioural context

Limited network intelligence

Large investigation workloads
```

As fraud techniques evolve, institutions require more adaptive and intelligence-driven monitoring capabilities.

---

# Industry Context

Financial crime detection increasingly relies on:

### Behavioural Analytics

Understanding:

```text
Transaction velocity

Customer behaviour

Counterparty relationships

Channel usage
```

rather than evaluating transactions in isolation.

---

### Graph Analytics

Modern financial crime often exhibits:

```text
Mule rings

Shared counterparties

Layering networks

Bridge accounts

Money movement communities
```

which are difficult to detect using transactional information alone.

---

### Explainable AI

Financial institutions require:

```text
Governance

Auditability

Regulatory transparency

Explainability
```

meaning models must provide clear reasoning behind risk decisions.

---

# Solution Approach

The solution combines:

## Behavioural Intelligence

Derived from:

```text
397,875,323 transactions
```

Examples:

```text
Transaction Velocity

Counterparty Concentration

Channel Concentration

Merchant Category Concentration

Money Flow Behaviour
```

Representative features:

```text
counterparty_entropy

avg_txn_per_day

channel_entropy

dominant_mcc_ratio

top_counterparty_transaction_share

top_counterparty_volume_share
```

---

## Customer & Account Intelligence

Examples:

```text
days_since_kyc

account_age_days

relationship_age_days

customer_age_days
```

These features identify:

```text
Customer maturity

Account maturity

KYC maintenance patterns
```

---

## Graph Intelligence

The framework constructs a graph:

```text
ACCOUNT
     →
COUNTERPARTY
```

containing:

```text
301,110 nodes

3,254,788 edges
```

Graph-based features capture:

```text
Community behaviour

Bridge behaviour

Neighbourhood characteristics

Relationship strength
```

Examples:

```text
betweenness_centrality

community_size

community_activity_score

neighbor_degree_mean

edge_amount_mean

edge_txn_count_std
```

---

# Model Development

Multiple modelling approaches were evaluated:

```text
LightGBM

XGBoost

Enhanced Tabular LightGBM

LightGBM + Graph Features

GraphSAGE

Graph Attention Networks (GAT)
```

All models were trained and evaluated using a frozen:

```text
70% Train

15% Validation

15% Test
```

framework to ensure fair comparison.

---

# Results and Findings

## Best Performing Model

### E4B – LightGBM + Extended Graph Features

Performance on unseen labelled data:

```text
ROC-AUC   = 0.9419

PR-AUC    = 0.7151

Precision = 0.7584

Recall    = 0.7602

F1        = 0.7593
```

---

## Key Finding #1

Enhanced behavioural features generated the largest performance improvement.

Examples:

```text
Counterparty Concentration

MCC Concentration

Transaction Velocity

Channel Behaviour
```

proved highly predictive.

---

## Key Finding #2

Graph-derived features provided significant additional predictive power.

Feature attribution analysis demonstrated:

```text
Tabular Features:
71.1%

Graph Features:
28.9%
```

Graph intelligence became one of the largest single contributors to model performance.

---

## Key Finding #3

Engineered graph intelligence outperformed Graph Neural Networks.

Models evaluated:

```text
GraphSAGE

GAT
```

did not exceed the performance of:

```text
LightGBM + Extended Graph Features
```

for this dataset.

This indicates that carefully engineered graph features may provide a more practical and explainable solution than deploying Graph Neural Networks in many institutional environments.

---

# Operational Client Use Case

The framework can be adapted for production deployment as follows:

```text
Incoming Transactions
          ↓
Feature Engineering
          ↓
Graph Construction
          ↓
Risk Scoring
          ↓
Investigation Queue
```

Evaluation and scoring can be executed:

```text
Hourly

Daily

Weekly
```

depending on operational requirements.

---

## Investigation Prioritisation

Instead of reviewing every account, investigators can focus on:

```text
Top 100

Top 500

Top 1000
```

highest-risk accounts.

This significantly improves investigation efficiency.

---

# Addressing Data Drift and Model Drift

## Data Drift

Occurs when customer behaviour changes over time.

Examples:

```text
Transaction values increase

New payment channels emerge

Digital adoption changes
```

Recommended controls:

```text
Population Stability Index (PSI)

Feature distribution monitoring

Monthly drift reviews
```

---

## Concept Drift

Occurs when fraud behaviour changes.

Examples:

```text
Different laundering patterns

Different mule strategies

Different transaction structures
```

Recommended controls:

```text
Quarterly model monitoring

Performance tracking

Analyst feedback review
```

---

## Graph Drift

Occurs when relationship structures change.

Examples:

```text
New fraud rings

New counterparty clusters

New community structures
```

Recommended controls:

```text
Community monitoring

Degree distribution monitoring

Graph feature re-computation
```

---

# Recommended Operating Model

## Monthly

Monitor:

```text
Feature Drift

Graph Drift

Score Distributions
```

---

## Quarterly

Evaluate:

```text
Precision

Recall

PR-AUC

Recall@500

Recall@1000
```

using newly investigated cases.

---

## Semi-Annual

Retrain using:

```text
Latest labelled accounts

Latest transactions

Latest graph structure
```

to maintain model relevance as fraud behaviour evolves.

---

# Benefits for Clients

This approach provides:

✅ Behaviour-based fraud detection

✅ Network-aware risk scoring

✅ Strong explainability

✅ Lower operational complexity than Graph Neural Networks

✅ Easier model governance

✅ Regulatory transparency

✅ Scalable deployment using standard analytics infrastructure

---

# Conclusion

The project demonstrates that a combination of:

```text
Behavioural Features

Customer Intelligence

Account Intelligence

Graph Intelligence
```

can significantly enhance mule account detection.

For financial institutions, the framework represents a practical and explainable approach to:

```text
Fraud Detection

Financial Crime Prevention

Risk Scoring

Investigation Prioritisation
```

while remaining operationally simpler and easier to govern than more complex Graph Neural Network architectures.

The final solution therefore serves as a strong client-facing example of how advanced analytics and graph intelligence can be operationalised to strengthen financial crime detection programmes.