# Cutoff Policy

Study Type

Retrospective Account Classification

Feature Window

All transaction history available
inside the released RBIH dataset.

Reason

The public challenge dataset
does not provide a validated
production scoring timestamp
for every account.

Current Assumption

All historical behaviour contained
within the released dataset is eligible
for feature generation.

Future Production Version

Use a fixed operational cutoff date T.

Only activity before T should be visible
to the model.