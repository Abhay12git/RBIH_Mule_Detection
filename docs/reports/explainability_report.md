
# E4B Explainability Report

Model:
LightGBM + Extended Graph Features

Metrics

ROC-AUC:
0.9312

PR-AUC:
0.6932

Precision:
0.7337

Recall:
0.7537

F1:
0.7436

## Top 20 Features

                           feature  importance
                    days_since_kyc        1330
                  edge_amount_mean        1183
                  account_age_days         991
                dominant_mcc_ratio         981
                edge_txn_count_std         872
            betweenness_centrality         784
                   edge_amount_max         781
                       branch_code         776
                   channel_entropy         759
                   avg_txn_per_day         737
                        branch_pin         729
           address_update_age_days         700
             unique_counterparties         664
                  avg_debit_amount         646
                 customer_age_days         639
     top_counterparty_volume_share         632
             relationship_age_days         617
top_counterparty_transaction_share         613
              neighbor_degree_mean         585
                       active_days         583

## Graph vs Tabular Contribution

feature_group  importance  importance_pct
      Tabular       22043       71.106452
        Graph        8957       28.893548

## Feature Family Importance

   feature_group  importance  importance_pct
           Graph        8957       32.098190
     Transaction        6433       23.053216
Enhanced_Tabular        4164       14.922057
        Customer        4075       14.603118
         Account        3117       11.170041
         Product        1159        4.153378

## Conclusions

1. KYC recency remains the strongest predictor.

2. Counterparty concentration features contribute significantly.

3. MCC concentration is highly predictive.

4. Graph structure contributes materially.

5. betweenness_centrality is the strongest graph signal.

6. Handcrafted graph features outperform GraphSAGE and GAT.
