import json

with open(
    "results/lightgbm_enhanced_metrics.json"
) as f:

    e3 = json.load(f)

with open(
    "results/lightgbm_graph_metrics.json"
) as f:

    e4 = json.load(f)

with open(
    "results/lightgbm_graph_extended_metrics.json"
) as f:

    e4b = json.load(f)

print()

print("=" * 70)
print("E3 vs E4 vs E4B")
print("=" * 70)

for metric in e3:

    print()

    print(metric)

    print(
        "E3 :",
        round(e3[metric],4)
    )

    print(
        "E4 :",
        round(e4[metric],4)
    )

    print(
        "E4B:",
        round(e4b[metric],4)
    )