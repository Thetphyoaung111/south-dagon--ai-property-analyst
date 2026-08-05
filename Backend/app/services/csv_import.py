import pandas as pd

from app.core.config import DATASET_FILE


def load_dataset():
    df = pd.read_csv(DATASET_FILE)

    print(f"Loaded {len(df)} properties")

    return df


if __name__ == "__main__":
    load_dataset()