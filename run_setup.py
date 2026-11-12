"""Run the full setup: load -> clean -> split -> save."""
from src.data_loader import load_raw
from src.preprocess import preprocess
from src.split import make_splits, save_splits


def main() -> None:
    raw = load_raw()
    clean = preprocess(raw)
    train, val, test = make_splits(clean)
    save_splits(train, val, test)

    print(f"Raw rows: {len(raw)} | Clean rows: {len(clean)}")
    for name, part in [("train", train), ("val", val), ("test", test)]:
        print(f"{name:5s}: {len(part):7d} rows | default rate {part['default'].mean():.2%}")


if __name__ == "__main__":
    main()
