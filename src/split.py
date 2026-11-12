"""Create stratified train / validation / test splits (70/15/15)."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

SEED = 42
OUT_DIR = Path("data/processed")


def make_splits(df: pd.DataFrame, target: str = "default"):
    """Return train, val, test dataframes with matching default rates."""
    train, temp = train_test_split(
        df, test_size=0.30, stratify=df[target], random_state=SEED
    )
    val, test = train_test_split(
        temp, test_size=0.50, stratify=temp[target], random_state=SEED
    )
    return train, val, test


def save_splits(train, val, test, out_dir: Path = OUT_DIR) -> None:
    """Write the three splits to CSV files."""
    out_dir.mkdir(parents=True, exist_ok=True)
    train.to_csv(out_dir / "train.csv", index=False)
    val.to_csv(out_dir / "val.csv", index=False)
    test.to_csv(out_dir / "test.csv", index=False)
