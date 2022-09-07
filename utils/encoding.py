import json
from pathlib import Path

import pandas as pd


def encode(csv_path: Path, csv_save_path: Path, json_save_path: Path):
    df = pd.read_csv(csv_path)
    encodings = {
        "sex": {"male": 1, "female": 0},
        "smoker": {"yes": 1, "no": 0},
    }
    df["sex"] = df["sex"].apply(lambda x: encodings["sex"][x])
    df["smoker"] = df["smoker"].apply(lambda x: encodings["smoker"][x])

    with open(json_save_path, "w", encoding="utf-8") as file:
        json.dump(encodings, file, indent=4)

    df.to_csv(csv_save_path, index=False)
