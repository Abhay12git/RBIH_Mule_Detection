import json

with open(
    "results/lightgbm_official_metrics.json"
) as f:

    e1 = json.load(f)

with open(
    "results/lightgbm_enhanced_metrics.json"
) as f:

    e3 = json.load(f)

print()

print("=" * 60)
print("LIGHTGBM COMPARISON")
print("=" * 60)

for metric in e1:

    print()

    print(metric)

    print(
        "E1:",
        round(e1[metric], 4)
    )

    print(
        "E3:",
        round(e3[metric], 4)
    )

    print(
        "Diff:",
        round(
            e3[metric] - e1[metric],
            4
        )
    )