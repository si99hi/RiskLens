"""Load the raw Give Me Some Credit training data."""
from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/cs-training.csv")


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Read the raw CSV and drop the unnamed index column."""
    if not Path(path).exists():
        raise FileNotFoundError(
            f"{path} not found. Download cs-training.csv from the Kaggle "
            "'Give Me Some Credit' competition and place it in data/raw/."
        )
    df = pd.read_csv(path)
    unnamed = [c for c in df.columns if c.startswith("Unnamed")]
    return df.drop(columns=unnamed)
