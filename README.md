# RiskLens

A credit risk scoring system that predicts loan default and explains every decision.

## Status
Step 1 of 4 complete: project setup, data cleaning and stratified splits.

## Setup
1. Create an environment: `python -m venv venv` then activate it
2. Install packages: `pip install -r requirements.txt`
3. Download `cs-training.csv` from the Kaggle "Give Me Some Credit" competition and place it in `data/raw/`
4. Run `python run_setup.py`
5. Open `notebooks/01_eda.ipynb` for exploration

## Structure
- `src/` reusable code (loading, cleaning, splitting)
- `notebooks/` exploration
- `data/` raw and processed data (raw data is not committed)
- `models/`, `app/`, `reports/` used in later steps

## Cleaning decisions
- Missing income and dependents filled with the median, with a missing flag kept
- Utilization and debt ratio capped at the 99th percentile
- Late payment counts capped at 20 (the data contains placeholder codes 96 and 98)
- Rows with age under 18 removed
- Splits are stratified 70/15/15 so each keeps the same default rate
