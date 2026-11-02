# Leakage Prevention Rules

## Target

is_mule

---

# Forbidden Columns

The following columns must NEVER be used as features.

## train_labels.parquet

mule_flag_date

alert_reason

flagged_by_branch

is_mule

---

# Future Information

Any information that becomes available after account flagging must not be used.

---

# Graph Features

Graph features must only use transaction history.

Label information must not be used during graph generation.

---

# Model Inputs

Allowed Sources:

accounts

customers

demographics

product_details

transactions

graph features

Forbidden Sources:

target variables

investigation outcomes

post-event flags