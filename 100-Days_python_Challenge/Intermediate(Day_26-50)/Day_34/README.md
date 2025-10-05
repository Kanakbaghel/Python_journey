# 100 Days of Code Challenge - Day 34: Data Cleaning and Preprocessing Basics

## Overview
Today, I learned **data cleaning and preprocessing** techniques in Pandas to transform raw, messy data into clean, usable formats. This includes removing duplicates, fixing data types, cleaning strings, handling dates, and basic transformations (e.g., renaming, sorting). Cleaning often takes 80% of data work but enables accurate analysis—think of it as "data hygiene."

Key focus: Iterative process: Inspect (e.g., `df.info()`), clean (e.g., `drop_duplicates()`), validate (e.g., check shapes/types). Always work on copies to avoid overwriting originals.

### What I Learned Today
- **Duplicates**:
  - Detect: `df.duplicated().sum()`.
  - Remove: `df.drop_duplicates(subset=['col1'], keep='first')` (first/last/False).
- **Data Types**:
  - Inspect: `df.dtypes`, `df.info()`.
  - Convert: `pd.to_numeric()`, `pd.to_datetime()`, `astype('category')`.
  - Coerce: `pd.to_numeric(..., errors='coerce')` (NaN for bad values).
- **String Cleaning**:
  - Access: `df['col'].str` (vectorized methods: `lower()`, `strip()`, `replace()`, `contains()`).
  - Regex: `str.replace(r'pattern', 'repl')` for advanced (e.g., remove punctuation).
- **Dates and Times**:
  - Convert: `pd.to_datetime(df['date_col'])`.
  - Extract: `.dt.year`, `.dt.month`; format with `strftime()`.
- **Other Preprocessing**:
  - Rename: `df.rename(columns={'old': 'new'})`.
  - Sort: `df.sort_values('col')`.
  - Reset index: `df.reset_index(drop=True)`.
  - Binning: `pd.cut(df['col'], bins=3)` for categorizing continuous data.
- **Best Practices**:
  - Chain operations: `df.pipe(clean_func1).pipe(clean_func2)`.
  - Log changes: Print shapes/info before/after each step.
  - Handle errors: Use `errors='ignore'` or try-except for robustness.
- **Common Pitfalls**: Assuming clean data (always inspect!); losing info during type conversion (use 'coerce').

Challenges: Dealing with inconsistent formats (e.g., dates as strings). Pro tip: Use `df.sample(10)` for quick visual checks!

### Code Example
The script `day34_pandas_cleaning.py` starts with a "messy" sales DataFrame and applies cleaning steps progressively.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`.
2. Save the Python code to `day34_pandas_cleaning.py`.
3. Run: `python day34_pandas_cleaning.py`.
