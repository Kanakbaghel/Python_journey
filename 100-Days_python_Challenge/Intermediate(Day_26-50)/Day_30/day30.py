# Day 30: DataFrame Indexing, Selection, and Filtering
# Import Pandas
import pandas as pd
import numpy as np

print("=== Day 30: Pandas DataFrame Indexing, Selection, and Filtering Demo ===\n")

# Sample DataFrame (from Day 29, extended)
data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David'],
    'Age': [22, 21, 23, 20],
    'Grade': [85.0, np.nan, 92.0, 75.0]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
print("Shape:", df.shape, "\n")

# 1. Column Selection
print("1. Column Selection")
# Single column (returns Series)
name_series = df['Name']
print("Select 'Name' column:\n", name_series)
print("Type:", type(name_series), "\n")  # <class 'pandas.core.series.Series'>

# Multiple columns (returns DataFrame)
subset_cols = df[['Name', 'Grade']]
print("Select ['Name', 'Grade']:\n", subset_cols, "\n")

# 2. Row Selection and Indexing
print("2. Row Selection and Indexing")

# Select specific rows by position (.iloc)
print(".iloc rows [0, 2]:\n", df.iloc[[0, 2]])  # Rows 0 and 2
print(".iloc single element (row 1, col 0):", df.iloc[1, 0], "\n")  # 'Bob'

# Select specific rows by label (.loc - default integer labels)
print(".loc rows [0, 3]:\n", df.loc[[0, 3]])
print(".loc slice (rows 0:2):\n", df.loc[0:2], "\n")  # Inclusive: rows 0,1,2

# Mixed: Rows by position, columns by label
print(".iloc rows [1:3], .loc cols 'Age':'Grade':\n", df.iloc[1:3].loc[:, 'Age':'Grade'])
# Or combined: df.loc[:, 'Age':'Grade'].iloc[1:3]
print("\nOutput:\n   Age  Grade\n1   21    NaN\n2   23   92.0")

# Single element access
print(".loc [2, 'Grade']:", df.loc[2, 'Grade'])  # 92.0
print(".iloc [2, 2]:", df.iloc[2, 2], "\n")  # Same: 92.0

# 3. Filtering (Boolean Indexing)
print("3. Filtering")

# Simple condition: Grade > 80 (ignores NaN)
high_grade = df[df['Grade'] > 80]
print("Filtered (Grade > 80):\n", high_grade)
print("Shape:", high_grade.shape, "\n")  # (2, 3)

# Multiple conditions (use & for AND, | for OR; parentheses required)
filtered_multi = df[(df['Age'] > 21) & (df['Grade'].notna())]
print("Filtered (Age > 21 AND Grade not null):\n", filtered_multi, "\n")

# Using query() for string conditions (cleaner for complex)
query_result = df.query('Age > 21 and Grade > 80')
print("Query (Age > 21 and Grade > 80):\n", query_result, "\n")  # Carol

# isin() for membership
names_filter = df[df['Name'].isin(['Alice', 'David'])]
print("Filtered by Name in ['Alice', 'David']:\n", names_filter, "\n")

# Filtering with NaN handling
nan_grade = df[df['Grade'].isna()]
print("Rows with NaN Grade:\n", nan_grade, "\n")  # Bob

# 4. Setting Values with Indexing
print("4. Setting Values")
# Conditional assignment (use .loc to avoid warnings)
df.loc[df['Grade'] < 80, 'Grade'] = 80  # Boost low grades
print("After boosting low grades:\n", df)
print("David's new Grade:", df.loc[3, 'Grade'], "\n")  # 80.0

# Fill NaN with mean (common cleaning)
mean_grade = df['Grade'].mean()
df['Grade'] = df['Grade'].fillna(mean_grade)
print("After filling NaN with mean (~87.25):\n", df)
print("All grades now non-null:", df['Grade'].isna().sum(), "\n")  # 0

# Add a new column based on condition
df['Passed'] = df['Grade'] >= 80
print("Added 'Passed' column (boolean):\n", df, "\n")

# 5. Practice Section - Try These!
print("5. Practice Exercises (Uncomment and Run)")
# Exercise 1: Even age and Grade > 80
# even_age_high = df[(df['Age'] % 2 == 0) & (df['Grade'] > 80)]
# print("Even age and high grade:\n", even_age_high)  # Alice (22 even, 85>80)

# Exercise 2: .iloc last two rows, first two cols
# last_two_first_cols = df.iloc[-2:, :2]
# print("Last two rows, first two cols:\n", last_two_first_cols)
# # Carol and David: Names and Ages

# Exercise 3: Replace NaN with mean (but we already did; try on copy)
# df_copy = df.copy()
# df_copy['Grade'] = df_copy['Grade'].fillna(df_copy['Grade'].mean())
# print("Copy with NaN filled:\n", df_copy)

print("=== End of Demo. Indexing and filtering unlock data insights! ===")
