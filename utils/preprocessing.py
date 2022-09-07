import pandas as pd
from pathlib import Path


def preprocess(
    csv_path: Path, labels_to_drop: list[str], save_path: Path
) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df.drop(labels_to_drop, axis=1, inplace=True)
    df.drop_duplicates(ignore_index=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(save_path, index=False)
