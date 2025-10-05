# Day 34: Data Cleaning and Preprocessing Basics
# Import Pandas and NumPy
import pandas as pd
import numpy as np

print("=== Day 34: Pandas Data Cleaning and Preprocessing Demo ===\n")

# Messy sample sales DataFrame (duplicates, wrong types, dirty strings, bad dates)
messy_data = {
    'ID': [1, 2, 2, 3, 4],  # Duplicate ID 2
    'Date': ['2023-01-15', '2023-01-16', '2023-01-16', 'Jan 17,23', '2023-01-18'],
    'Region': ['North', ' South', ' South', 'East', 'north'],  # Leading/trailing spaces, mixed case
    'Product': ['Laptop', 'Phone', 'Phone', 'Laptop!!!', 'Mouse'],
    'Sales': ['1000', '500.5', '500.5', '900', 'abc'],  # String with invalid 'abc'
    'Quantity': [1, 2, 2, 1, 5]
}
df_messy = pd.DataFrame(messy_data)
print("Messy Original DataFrame:\n", df_messy)
print("Shape:", df_messy.shape, "\n")  # (5, 6)

# Work on a copy for cleaning
df = df_messy.copy()

# 1. Inspect Data (Always Start Here!)
print("1. Initial Inspection")
print("Info:\n")
df.info()
# Shows types, non-null counts (all 5 here, but we'll add issues)

print("\nSample:\n", df.sample(3))  # Random sample for quick look

# 2. Handle Duplicates
print("\n2. Handling Duplicates")
dup_count = df.duplicated().sum()
print(f"Duplicates detected: {dup_count}")  # 1 (row 2)

df_no_dups = df.drop_duplicates(keep='first')  # Keep first occurrence
print("After drop duplicates: Shape", df_no_dups.shape, "\n")  # (4, 6)
df = df_no_dups  # Update df

# Subset duplicates (e.g., only on ID and Product)
# df.drop_duplicates(subset=['ID', 'Product'], keep='last')

# 3. Fix Data Types
print("3. Fixing Data Types")
print("Data types before:\n", df.dtypes)
# ID: int64, Date: object, Sales: object (needs numeric)

# Convert Sales to numeric (coerce errors to NaN)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
print("After cleaning Sales to numeric:", df['Sales'].tolist())
# [1000.0, 500.5, 900.0, NaN] - 'abc' becomes NaN

# Convert Date to datetime (coerce invalid)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')  # Handles mixed formats
print("Dates converted:\n", df['Date'].tolist(), "\n")  # Parses 'Jan 17,23' to 2023-01-17

# Convert Region to category (for memory efficiency if limited unique values)
df['Region'] = df['Region'].astype('category')
print("Region as category dtype:", df['Region'].dtype, "\n")  # category

# 4. String Cleaning
print("4. String Cleaning")
# Before cleaning Product (has '!!!')
print("Product before:", df['Product'].tolist())

# Vectorized string ops
df['Product'] = df['Product'].str.strip().str.replace('!!!', '', regex=False)  # Remove trailing ! and spaces
print("Product after strip/replace:", df['Product'].tolist())  # ['Laptop', 'Phone', 'Laptop', 'Mouse']

# Region: Strip spaces, standardize case
df['Region'] = df['Region'].str.strip().str.title()  # ' South' -> 'South', 'north' -> 'North'
print("Region after cleaning:\n", df['Region'].tolist(), "\n")  # ['North', 'South', 'East', 'North']

# Advanced: Regex to remove non-alphanumeric from Product
# df['Product'] = df['Product'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# 5. Date Preprocessing
print("5. Date Preprocessing")
# Extract components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
print("Extracted Year and Month:\n", df[['Date', 'Year', 'Month']].head(), "\n")

# Format dates as strings if needed
df['Formatted_Date'] = df['Date'].dt.strftime('%Y-%m-%d')
print("Formatted Date:\n", df['Formatted_Date'].tolist())

# 6. Other Preprocessing
print("6. Other Preprocessing")

# Rename columns
df = df.rename(columns={'ID': 'Order_ID', 'Sales': 'Revenue'})
print("Renamed columns. New names:", df.columns.tolist(), "\n")

# Sort by Date
df = df.sort_values('Date').reset_index(drop=True)
print("Sorted by Date and reset index:\n", df[['Date', 'Order_ID']], "\n")

# Binning: Categorize Revenue
bins = [0, 600, 900, np.inf]
labels = ['Low', 'Medium', 'High']
df['Revenue_Binned'] = pd.cut(df['Revenue'], bins=bins, labels=labels)
print("Revenue binned:\n", df['Revenue_Binned'].tolist(), "\n")  # ['Low', 'Medium', 'High', 'Low'] (NaN as Low)

# 7. Final Cleaned DataFrame
print("7. Final Cleaned DataFrame")
print(df)
print("\nFinal shape:", df.shape)
print("Final dtypes:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())  # Revenue: 1 (from 'abc')

# Summary stats after cleaning
print("\nCleaned summary:\n", df.describe(include='all'))

# 8. Practice Section - Try These!
print("\n8. Practice Exercises (Uncomment and Run)")
# Exercise 1: Standardize Region to title case (already similar; extend to all strings)
# df['Region'] = df['Region'].str.title()
# print("Title case Region:\n", df['Region'])

# Exercise 2: Bin Quantity into 'Low' (1-2), 'Medium' (3-4), 'High' (5+)
# qty_bins = [0, 2, 4, np.inf]
# qty_labels = ['Low', 'Medium', 'High']
# df['Quantity_Bin'] = pd.cut(df['Quantity'], bins=qty_bins, labels=qty_labels)
# print("Quantity binned:\n", df['Quantity_Bin'])

# Exercise 3: Handle invalid dates (add bad date) and extract year
# df.loc[4, 'Date'] = 'invalid-date'
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# df['Year'] = df['Date'].dt.year
# print("Year after coerce:\n", df['Year'])

print("=== End of Demo. Clean data powers great analysis! ===")
