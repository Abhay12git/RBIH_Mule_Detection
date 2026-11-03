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