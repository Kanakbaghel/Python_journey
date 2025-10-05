# 100 Days of Code Challenge - Day 30: DataFrame Indexing, Selection, and Filtering

## Overview
Today, I practiced **indexing, selection, and filtering** in Pandas DataFrames. Indexing accesses rows/columns by label or position, selection grabs subsets (e.g., specific columns), and filtering uses conditions to subset rows (e.g., "show students with grades > 80"). These operations are vectorized (fast, like NumPy) and use boolean masks for efficiency.

Key focus: Mastering `.loc` (label-based), `.iloc` (position-based), column selection, and conditional filtering. Avoid common errors like mixing label/position access.

### What I Learned Today
- **Indexing**:
  - `.loc[]`: Label-based (e.g., `df.loc[0, 'Name']` or `df.loc[0:2, 'Age':'Grade']` for slices).
  - `.iloc[]`: Position-based (e.g., `df.iloc[0, 1]` for row 0, col 1; slices like lists).
  - Slicing: Inclusive on both ends for `.loc` (unlike Python lists); exclusive for `.iloc`.
- **Selection**:
  - Single column: `df['Name']` (returns Series).
  - Multiple columns: `df[['Name', 'Grade']]` (returns DataFrame).
  - Rows: `df.loc[[0, 2]]` or `df.iloc[[0, 2]]`.
- **Filtering**:
  - Boolean indexing: `df[df['Grade'] > 80]` (mask from condition).
  - Multiple conditions: `df[(df['Age'] > 20) & (df['Grade'].notna())]`.
  - `df.query('Grade > 80')`: String-based for readability.
  - `isin()`: `df[df['Name'].isin(['Alice', 'Bob'])]`.
  - Setting values: `df.loc[df['Grade'] < 70, 'Grade'] = 70` (conditional assignment).
- **Advanced Tips**:
  - Chaining: `df.loc[df['Grade'] > 80, ['Name', 'Grade']]`.
  - Avoid: Direct assignment like `df[0] = value` (deprecated); use `.loc`/`.iloc`.
  - Efficiency: Filtering creates views/copies—use `.copy()` if modifying subsets.
- **Common Pitfalls**: KeyError for missing labels; SettingWithCopyWarning (use `.loc` to avoid).

Challenges: Balancing label vs. position when indices are custom. Pro tip: Reset index with `df.reset_index()` if needed!

### Code Example
The script `day30_pandas_indexing.py` uses a sample student DataFrame. It demonstrates selection, indexing, and filtering with outputs.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`.
2. Save the Python code to `day30_pandas_indexing.py`.
3. Run: `python day30_pandas_indexing.py`.

### Output Preview
The script outputs like:

Original DataFrame: Name Age Grade 0 Alice 22 85.0 1 Bob 21 NaN 2 Carol 23 92.0 3 David 20 75.0

Select 'Name' column: 0 Alice 1 Bob 2 Carol 3 David Name: Name, dtype: object

.loc slice (rows 0:2, cols 'Age':'Grade'): Age Grade 0 22 85.0 1 21 NaN

.iloc position (row 2, col 1): 92.0

Filtered (Grade > 80): Name Age Grade 0 Alice 22 85.0 2 Carol 23 92.0

Query (Age > 21 and Grade not null): Name Age Grade 2 Carol 23 92.0