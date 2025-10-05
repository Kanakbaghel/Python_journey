# 100 Days of Code Challenge - Day 31: Handling Missing Data in Pandas

## Overview
Today, I learned how to handle **missing data** in Pandas—values like NaN (Not a Number) or None that can skew analysis or cause errors. Missing data is common in real datasets (e.g., surveys, sensors). Pandas provides tools to detect, drop, or fill them strategically, preserving as much data as possible.

Key focus: Detection with `isna()`, removal with `dropna()`, and imputation with `fillna()`. Always decide based on context: Drop if <5% missing; fill otherwise (e.g., mean for numerics, forward-fill for time series).

### What I Learned Today
- **Detecting Missing Data**:
  - `df.isna()` or `df.isnull()`: Boolean mask for NaNs.
  - `df.notna()`: Opposite (non-missing).
  - `df.info()`: Shows non-null counts per column.
  - `df.isnull().sum()`: Count missing per column.
  - Specific: `df['col'].isna().sum()` or `df[df['col'].isna()]` (rows with missing in col).
- **Removing Missing Data**:
  - `df.dropna()`: Drops rows/columns with NaNs.
    - `axis=0` (rows, default), `axis=1` (columns).
    - `how='any'` (drop if any NaN, default), `'all'` (drop if all NaN).
    - `thresh=2`: Drop if <2 non-null values.
    - `subset=['col1', 'col2']`: Only consider these columns.
  - Returns a new DataFrame (use `inplace=True` to modify original).
- **Filling Missing Data**:
  - `df.fillna(value)`: Replace with scalar (e.g., 0), dict (per column), or method.
  - Methods: `'ffill'` (forward-fill: use previous value), `'bfill'` (backward-fill), `'pad'`.
  - Statistical: `df.fillna(df.mean())` (column means for numerics).
  - Advanced: `df.interpolate()` (linear for time series).
  - For categoricals: `df['col'].fillna('Unknown')`.
- **Best Practices**:
  - Check % missing: `(df.isnull().sum() / len(df)) * 100`.
  - Impute wisely: Mean/median for skewed data; mode for categoricals.
  - Chain ops: `df.dropna().fillna(0)`.
- **Common Pitfalls**: NaN in floats/integers; `None` becomes NaN. Dropping too much loses data—visualize first (e.g., with Matplotlib later).

Challenges: Choosing fill method (e.g., ffill for sequences). Pro tip: Use `df.info()` before/after to track changes!

### Code Example
The script `day31_pandas_missing_data.py` uses a sample DataFrame with NaNs in grades and attendance. It shows detection, dropping, and filling.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`.
2. Save the Python code to `day31_pandas_missing_data.py`.
3. Run: `python day31_pandas_missing_data.py`.

