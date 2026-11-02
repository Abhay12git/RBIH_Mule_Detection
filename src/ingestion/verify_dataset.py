from pathlib import Path

root = Path("data/raw")

for file in root.rglob("*"):
    print(file)