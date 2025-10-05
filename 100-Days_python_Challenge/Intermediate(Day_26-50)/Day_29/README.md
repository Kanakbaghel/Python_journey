# 100 Days of Code Challenge - Day 29: Introduction to Pandas: Series and DataFrames

## Overview
Today, I started with **Pandas**, a library for data manipulation and analysis. It excels at handling real-world data (e.g., spreadsheets, time series) with labeled indices and missing values support. Core structures: **Series** (like a labeled NumPy array) and **DataFrame** (like a labeled 2D table with rows/columns).

Key focus: Creating and inspecting these structures. Pandas uses NumPy under the hood for efficiency but adds labels (indices) for intuitive access.

### What I Learned Today
- **Importing Pandas**: `import pandas as pd` (standard alias).
- **Pandas Series**:
  - 1D array with index labels (default: integers 0,1,2...).
  - Create from: List (`pd.Series([1,2,3])`), dict (`pd.Series({'a':1, 'b':2})`), scalar (`pd.Series(5, index=['a','b'])`).
  - Attributes: `series.index`, `series.values` (NumPy array), `series.dtype`, `series.shape`.
  - Access: `series['label']` or `series[0]` (position).
- **Pandas DataFrames**:
  - 2D table with row index and column labels.
  - Create from: Dict of lists (`pd.DataFrame({'col1': [1,2], 'col2': [3,4]})`), list of dicts, Series, or even NumPy arrays.
  - Attributes: `df.index` (rows), `df.columns`, `df.shape`, `df.dtypes`.
  - Viewing: `df.head(3)` (first n rows), `df.tail()`, `df.info()` (summary), `df.describe()` (stats).
- **Key Differences from NumPy**:
  - Labels over positions: `df.loc['row_label']` vs. `df.iloc[0]` (integer position).
  - Handles missing data: `pd.NaT`, `np.nan`.
  - Axis: 0=rows (down), 1=columns (across).
- **Why Pandas?** Easy data cleaning/loading; integrates with NumPy, Matplotlib, and more. Great for ETL (Extract, Transform, Load) pipelines.

Challenges: Grasping index vs. position access. Pro tip: Use `df.head()` early to verify structure!

### Code Example
The script `day29_pandas_intro.py` demonstrates creation and inspection of Series and DataFrames. It includes sample data mimicking a "student grades" dataset.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`.
2. Save the Python code to `day29_pandas_intro.py`.
3. Run: `python day29_pandas_intro.py`.

### Output Preview
The script outputs like:

Series from list: 0 10 1 20 2 30 dtype: int64

Series values: [10 20 30] Shape: (3,)

DataFrame: Name Age Grade 0 Alice 22 85.0 1 Bob 21 NaN 2 Carol 23 92.0

First 2 rows: Name Age Grade 0 Alice 22 85.0 1 Bob 21 NaN

Info: <class 'pandas.core.frame.DataFrame'> RangeIndex: 3 entries, 0 to 2 Data columns (total 3 columns):

Column Non-Null Count Dtype
0 Name 3 non-null object 1 Age 3 non-null int64
2 Grade 2 non-null float64 dtypes: float64(1), int64(1), object(1) memory usage: 200.0+ bytes


