"""Clean the raw data: rename, fill missing values, cap outliers."""
import pandas as pd

RENAME = {
    "SeriousDlqin2yrs": "default",
    "RevolvingUtilizationOfUnsecuredLines": "utilization",
    "age": "age",
    "NumberOfTime30-59DaysPastDueNotWorse": "late_30_59",
    "DebtRatio": "debt_ratio",
    "MonthlyIncome": "monthly_income",
    "NumberOfOpenCreditLinesAndLoans": "open_credit_lines",
    "NumberOfTimes90DaysLate": "late_90",
    "NumberRealEstateLoansOrLines": "real_estate_loans",
    "NumberOfTime60-89DaysPastDueNotWorse": "late_60_89",
    "NumberOfDependents": "dependents",
}

LATE_COLS = ["late_30_59", "late_60_89", "late_90"]
CAP_COLS = ["utilization", "debt_ratio"]
FILL_COLS = ["monthly_income", "dependents"]


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw dataframe."""
    df = df.rename(columns=RENAME).copy()

    # Drop rows with impossible ages.
    df = df[df["age"] >= 18]

    # Missing values: add a flag, then fill with the median.
    for col in FILL_COLS:
        df[f"{col}_was_missing"] = df[col].isna().astype(int)
        df[col] = df[col].fillna(df[col].median())

    # Cap extreme outliers at the 99th percentile.
    for col in CAP_COLS:
        df[col] = df[col].clip(upper=df[col].quantile(0.99))

    # Late payment columns contain placeholder codes (96, 98). Cap at 20.
    for col in LATE_COLS:
        df[col] = df[col].clip(upper=20)

    return df.reset_index(drop=True)
