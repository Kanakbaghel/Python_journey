# 100 Days of Code Challenge - Day 33: Merging, Joining, and Concatenating DataFrames

## Overview
Today, I practiced **combining DataFrames** in Pandas: concatenation for simple stacking, merging for key-based joins (like SQL), and joining for index-aligned merges. These operations are crucial for real-world data workflows, such as linking customer data with orders or appending datasets from multiple files.

Key focus: Understanding when to use each method and handling join types (inner, left, outer). Merging preserves relationships via keys; concatenation ignores them.

### What I Learned Today
- **Concatenation (`pd.concat()`)**:
  - Stacks DataFrames: `axis=0` (vertical, rows), `axis=1` (horizontal, columns).
  - Options: `ignore_index=True` (reset index), `join='inner'` (intersect columns), `keys=['df1', 'df2']` (multi-index).
  - For lists of DataFrames: `pd.concat([df1, df2])`.
- **Merging (`pd.merge()`)**:
  - Like SQL JOIN: `pd.merge(df1, df2, on='key')` (same key name) or `left_on='key1', right_on='key2'`.
  - How: `'inner'` (intersection, default), `'left'` (all from left), `'right'` (all from right), `'outer'` (union).
  - Suffixes: `suffixes=('_left', '_right')` for duplicate columns.
  - Multi-keys: `on=['key1', 'key2']`.
- **Joining (`df.join()`)**:
  - Index-based: `df1.join(df2)` (merges on index; like merge with `left_index=True, right_index=True`).
  - How: Same as merge (`how='left'`, etc.).
  - Useful for time series or when keys are indices.
- **Best Practices**:
  - Validate: Check shapes with `df.shape` before/after; use `validate='one_to_many'` for integrity.
  - Handle duplicates: `pd.merge(..., indicator=True)` to see join source.
  - Memory: For large data, merge on sorted keys or use Dask.
- **Common Pitfalls**: Key mismatches cause NaNs or lost data; always specify `how` explicitly. Concat on mismatched columns adds NaNs.

Challenges: Choosing join type to avoid data loss. Pro tip: Use `pd.merge(..., indicator=True)` to debug overlaps!

### Code Example
The script `day33_pandas_merging.py` uses "students" and "enrollments" DataFrames. It demonstrates concat, merge, and join with different scenarios.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`.
2. Save the Python code to `day33_pandas_merging.py`.
3. Run: `python day33_pandas_merging.py`.
