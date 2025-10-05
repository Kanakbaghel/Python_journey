# 100 Days of Code Challenge - Day 32: Pandas Grouping and Aggregation

## Overview
Today, I explored **grouping and aggregation** in Pandas using `groupby()`. This splits a DataFrame into groups based on one or more columns (e.g., by 'Major'), applies functions (e.g., mean, sum), and combines results into a new structure. It's perfect for summarizing data, like calculating average grades by department or total sales by category.

Key focus: Basic `groupby()`, aggregation methods (`agg()`, `apply()`), and handling multi-level groups. Aggregation reduces data size while revealing patterns—essential for reports and EDA (Exploratory Data Analysis).

### What I Learned Today
- **GroupBy Basics**:
  - `df.groupby('column')`: Groups by a single column (returns GroupBy object).
  - Access groups: `grouped.groups` (dict of labels to indices), `grouped.get_group('label')`.
  - Iterate: `for name, group in grouped: ...` (name=group key, group=subset DataFrame).
- **Aggregation**:
  - Built-in: `grouped.mean()`, `sum()`, `count()`, `min()`, `max()`, `std()` (applies to numerics by default).
  - Custom: `grouped.agg('mean')` or `grouped.agg({'col1': 'mean', 'col2': 'sum'})` (dict for per-column).
  - Multiple functions: `grouped.agg(['mean', 'std'])` (multi-level columns) or `grouped.agg({'col': ['mean', 'sum']})`.
  - `transform()`: Apply function but keep shape (e.g., add group mean as new column).
  - `apply()`: Custom functions on groups (flexible but slower).
- **Multi-Level Grouping**:
  - `df.groupby(['col1', 'col2'])`: Groups by combinations (hierarchical index).
  - `as_index=False`: Keep groups as columns, not index.
- **Best Practices**:
  - Handle NaNs: GroupBy skips them by default; use `dropna()` first if needed.
  - Reset index: `grouped.mean().reset_index()` for flat DataFrame.
  - For categoricals: Use `pd.Categorical` for ordered groups.
- **Common Pitfalls**: Non-numeric columns ignored in simple agg; use `agg()` for specifics. Large groups can be memory-intensive—sample data first.

Challenges: Understanding multi-index outputs. Pro tip: Use `grouped.size()` to see group sizes before aggregating!

### Code Example
The script `day32_pandas_groupby.py` uses a sample student DataFrame with 'Major' for grouping. It shows aggregation, multi-functions, and transformations.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`.
2. Save the Python code to `day32_pandas_groupby.py`.
3. Run: `python day32_pandas_groupby.py`.
