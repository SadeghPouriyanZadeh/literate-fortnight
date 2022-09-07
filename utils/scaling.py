import json
from pathlib import Path

import pandas as pd


def scale(csv_path: Path, json_save_path: Path, csv_save_path: Path):
    df = pd.read_csv(csv_path)

    continuos_columns = ["age", "bmi", "charges", "children"]
    stats = {}
    for col in df.columns:
        if col in continuos_columns:
            stats[col] = {"mean": df[col].mean(), "std": df[col].std()}

    for i in stats:
        if i in continuos_columns:
            df[i] = (df[i] - stats[i]["mean"]) / stats[i]["std"]
    with open(json_save_path, "w") as f:
        json.dump(stats, f, indent=4)
    df.to_csv(csv_save_path, index=False)
