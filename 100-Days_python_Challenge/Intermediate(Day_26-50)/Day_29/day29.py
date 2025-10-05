# Day 29: Introduction to Pandas: Series and DataFrames
# Import Pandas (and NumPy for reference)
import pandas as pd
import numpy as np

print("=== Day 29: Pandas Series and DataFrames Intro Demo ===\n")

# 1. Pandas Series
print("1. Creating and Inspecting Series")

# Series from a list (default integer index)
series_list = pd.Series([10, 20, 30])
print("Series from list:\n", series_list)
print("Series values (NumPy array):", series_list.values)
print("Index:", series_list.index)
print("Data type:", series_list.dtype)
print("Shape:", series_list.shape, "\n")

# Access elements
print("Access by position [1]:", series_list[1])  # 20
print("Access by slice [0:2]:\n", series_list[0:2], "\n")

# Series from a dictionary (custom index labels)
series_dict = pd.Series({'Alice': 85, 'Bob': 92, 'Carol': 78})
print("Series from dict:\n", series_dict)
print("Access by label 'Bob':", series_dict['Bob'], "\n")  # 92

# Series from scalar (broadcasts value to index length)
series_scalar = pd.Series(100, index=['x', 'y', 'z'])
print("Series from scalar:\n", series_scalar, "\n")

# Series with NaN (missing value)
series_with_nan = pd.Series([1, np.nan, 3])
print("Series with NaN:\n", series_with_nan)
print("Check NaN:", series_with_nan.isna(), "\n")  # [False  True False]

# 2. Pandas DataFrames
print("2. Creating and Inspecting DataFrames")

# DataFrame from dictionary of lists (columns as keys)
data_dict = {
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [22, 21, 23],
    'Grade': [85.0, np.nan, 92.0]  # Include a missing value
}
df_dict = pd.DataFrame(data_dict)
print("DataFrame from dict:\n", df_dict)
print("Shape:", df_dict.shape)  # (3, 3)
print("Columns:", df_dict.columns)
print("Index:", df_dict.index, "\n")

# Access: By column label
print("Column 'Name':\n", df_dict['Name'])
print("Row 0 (position):\n", df_dict.iloc[0])
print("Row by index label 1:\n", df_dict.loc[1], "\n")  # Bob's row

# DataFrame from list of dictionaries (each dict is a row)
data_list_of_dicts = [
    {'Name': 'David', 'Age': 20, 'Grade': 88},
    {'Name': 'Eve', 'Age': 24, 'Grade': 95}
]
df_list = pd.DataFrame(data_list_of_dicts)
print("DataFrame from list of dicts:\n", df_list, "\n")

# DataFrame from NumPy array (with custom columns/index)
np_array = np.array([[1, 2], [3, 4], [5, 6]])
df_np = pd.DataFrame(np_array, columns=['A', 'B'], index=['row1', 'row2', 'row3'])
print("DataFrame from NumPy array:\n", df_np, "\n")

# 3. Basic Inspection Methods
print("3. Basic Inspection")
print("Full DataFrame (from dict):\n", df_dict)

print("\nFirst 2 rows (head()):\n", df_dict.head(2))
print("\nLast 2 rows (tail()):\n", df_dict.tail(2))

print("\nData types (dtypes):\n", df_dict.dtypes)
# Output:
# Name     object
# Age       int64
# Grade   float64
# dtype: object

print("\nSummary info (info()):\n")
df_dict.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   Name    3 non-null      object 
#  1   Age     3 non-null      int64  
#  2   Grade   2 non-null      float64
# dtypes: float64(1), int64(1), object(1)
# memory usage: 200.0+ bytes

print("\nDescriptive stats (describe()):\n")
print(df_dict.describe())
#        Age      Grade
# count  3.0   2.000000
# mean  22.0  88.500000
# std    1.0   5.000000
# ...

# Transpose (rows to columns)
print("\nTransposed:\n", df_dict.T, "\n")  # Columns become rows

# 4. Practice Section - Try These!
print("4. Practice Exercises (Uncomment and Run)")
# Exercise 1: Series from dict with custom access
# my_series = pd.Series({'math': 90, 'science': 85}, index=['science', 'math'])
# print("Custom Series:\n", my_series)
# print("Access 'math':", my_series['math'])

# Exercise 2: DataFrame from list of dicts + head/describe
# sales_data = [{'product': 'A', 'sales': 100}, {'product': 'B', 'sales': 150}]
# sales_df = pd.DataFrame(sales_data)
# print("Sales DF head:\n", sales_df.head())
# print("Sales describe:\n", sales_df.describe())

# Exercise 3: Add column to DF (scalar)
# df_dict['Status'] = 'Pass'  # Adds 'Pass' to every row
# print("DF with new column:\n", df_dict)

print("=== End of Demo. Pandas makes data handling intuitive! ===")
