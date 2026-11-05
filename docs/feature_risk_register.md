# Feature Risk Register

## SAFE

txn_count

credit_count

debit_count

active_days

unique_counterparties

customer_age_days

relationship_age_days

avg_balance

UPC_count

UPD_count

## REVIEW

account_status

days_since_kyc

days_since_mobile_update

address_update_age_days

passbook_update_age_days

## DROP

is_mule

mule_flag_date

alert_reason

flagged_by_branch

freeze_date

unfreeze_date

## Notes

DROP features must never be used for training.

REVIEW features require business validation
before production deployment.

## Graph Feature Risk Assessment

SAFE

- out_degree
- weighted_degree
- neighbor_count
- community_id
- community_size
- neighbor_degree_mean
- betweenness_centrality
- community_activity_score

REVIEW

- pagerank
- two_hop_neighbor_count
- neighbor_degree_max

Reason

Potential saturation observed.

Will be evaluated during Stage 13.
## Graph Feature Assessment

APPROVED

- betweenness_centrality
- neighbor_degree_mean
- community_activity_score
- community_id
- community_size

REVIEW

- pagerank
- two_hop_neighbor_count
- neighbor_degree_max

Reason

Weaker contribution based on LightGBM graph feature importance analysis.

Retained for future evaluation.