# Day 31: Handling Missing Data in Pandas
# Import Pandas and NumPy
import pandas as pd
import numpy as np

print("=== Day 31: Pandas Missing Data Handling Demo ===\n")

# Sample DataFrame with missing values (NaN)
data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [22, 21, 23, 20, 24],
    'Grade': [85.0, np.nan, 92.0, np.nan, 88.0],
    'Attendance': [np.nan, 90.0, 95.0, np.nan, np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
print("Shape:", df.shape, "\n")  # (5, 4)

# 1. Detecting Missing Data
print("1. Detecting Missing Data")

# Boolean mask for all NaNs
print("NaN mask (isna()):\n", df.isna())
# Output: True where NaN

# Count missing per column
missing_counts = df.isnull().sum()
print("Missing counts per column:\n", missing_counts)
# Name: 0
# Age: 0
# Grade: 2
# Attendance: 2

# Percentage missing
missing_pct = (df.isnull().sum() / len(df)) * 100
print("\n% Missing:\n", missing_pct)
# Grade: 20.0
# Attendance: 20.0

# Rows with missing in specific column
print("\nRows with NaN in 'Grade':\n", df[df['Grade'].isna()])
# Bob and David

# Use info() for summary (non-null counts)
print("\nDataFrame info:\n")
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   Name         5 non-null      object 
#  1   Age          5 non-null      int64  
#  2   Grade        3 non-null      float64
#  3   Attendance   2 non-null      float64
# dtypes: float64(2), int64(1), object(1)
# memory usage: 288.0+ bytes

# 2. Removing Missing Data
print("\n2. Removing Missing Data")

# Drop rows with any NaN (default: axis=0, how='any')
df_dropped_rows = df.dropna()
print("Rows with any NaN (dropped):\n", df_dropped_rows)
# Only Carol (row 2) - complete row

# Drop columns with any NaN
df_dropped_cols = df.dropna(axis=1)
print("Columns with any NaN (dropped):\n", df_dropped_cols)
# Only Name and Age (no NaNs)

# Drop rows only if all NaN (how='all')
df_drop_all = df.dropna(how='all')
print("Drop rows if ALL NaN:\n", df_drop_all)
# Same as original (no row has all NaN)

# Threshold: Drop rows with <3 non-null
df_thresh = df.dropna(thresh=3)
print("Drop rows with <3 non-null:\n", df_thresh)
# Drops David (row 3: only Name and Age non-null)

# Subset: Drop if NaN in specific columns
df_subset = df.dropna(subset=['Grade', 'Attendance'])
print("Drop if NaN in Grade or Attendance:\n", df_subset)
# Only Carol

# Inplace modification (modifies original - use carefully!)
# df.dropna(inplace=True)  # Would shrink df to 1 row

# 3. Filling Missing Data
print("\n3. Filling Missing Data")

# Fill all NaN with a scalar (e.g., 0)
df_filled_0 = df.fillna(0)
print("All NaN filled with 0:\n", df_filled_0)

# Fill per column (dict: different values)
df_filled_dict = df.fillna({'Grade': df['Grade'].mean(), 'Attendance': 0})
mean_grade = df['Grade'].mean()  # ~88.333
print(f"\nAfter filling Grade with mean ({mean_grade:.2f}) and Attendance with 0:\n", df_filled_dict)

# Method-based: Forward fill (ffill) - use previous value
df_ffill = df.copy()  # Work on copy
df_ffill['Attendance'] = df_ffill['Attendance'].ffill()  # Alice gets NaN (no prev), Bob=90, etc.
print("\nForward fill on Attendance (sequential assumption):\n", df_ffill['Attendance'])
# Note: First NaN stays NaN; better for time series

# Backward fill (bfill)
df_bfill = df.copy()
df_bfill['Grade'] = df_bfill['Grade'].bfill()
print("\nBackward fill on Grade:\n", df_bfill['Grade'])
# David gets 88.0 (from Eve), Bob gets David's (but since NaN, propagates)

# Statistical fill for numerics (mean, median)
df_mean_fill = df.copy()
numeric_cols = ['Grade', 'Attendance']
for col in numeric_cols:
    df_mean_fill[col] = df_mean_fill[col].fillna(df_mean_fill[col].mean())
print("\nFill numerics with column means:\n", df_mean_fill[numeric_cols])

# For categoricals (e.g., if 'Name' had NaN)
# df['Name'] = df['Name'].fillna('Unknown')

# Interpolation (linear - for sequential data)
df_interp = df.copy()
df_interp['Attendance'] = df_interp['Attendance'].interpolate(method='linear')
print("\nLinear interpolation on Attendance:\n", df_interp['Attendance'])
# Estimates between known values (e.g., Alice ~92.5 if assuming linear from Bob=90, Carol=95)

# 4. Combined Workflow (Clean a Copy)
print("\n4. Combined Example: Clean DataFrame")
df_clean = df.copy()
# Step 1: Drop rows with too many NaNs (thresh=3)
df_clean = df_clean.dropna(thresh=3)
# Step 2: Fill remaining NaNs
df_clean['Grade'] = df_clean['Grade'].fillna(df_clean['Grade'].mean())
df_clean['Attendance'] = df_clean['Attendance'].fillna(0)
print("Cleaned DataFrame (dropped 1 row, filled rest):\n", df_clean)
print("Final shape:", df_clean.shape, "\n")  # (4, 4)

# 5. Practice Section - Try These!
print("5. Practice Exercises (Uncomment and Run)")
# Exercise 1: Drop columns with >20% missing
# missing_threshold = (df.isnull().sum() / len(df)) > 0.2
# cols_to_drop = missing_threshold[missing_threshold].index
# df_dropped_cols = df.drop(columns=cols_to_drop)
# print("Dropped high-missing cols:\n", df_dropped_cols)

# Exercise 2: Forward-fill Attendance on full df
# df_ffill_full = df.copy()
# df_ffill_full['Attendance'] = df_ffill_full['Attendance'].ffill().bfill()  # ffill then bfill first NaN
# print("Full ffill + bfill on Attendance:\n", df_ffill_full['Attendance'])

# Exercise 3: Fill 'Name' (add NaN first) and mean Grade
# df_practice = df.copy()
# df_practice.loc[1, 'Name'] = np.nan  # Add a missing Name
# df_practice['Name'] = df_practice['Name'].fillna('Unknown')
# df_practice['Grade'] = df_practice['Grade'].fillna(df_practice['Grade'].mean())
# print("Practice filled:\n", df_practice)

print("=== End of Demo. Clean data leads to better insights! ===")
