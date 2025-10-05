# Day 32: Data Aggregation and groupby in Pandas
# Import Pandas and NumPy
import pandas as pd
import numpy as np

print("=== Day 32: Pandas Data Aggregation with groupby Demo ===\n")

# Sample sales DataFrame for aggregation examples
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Sales': [100, 150, 200, 120, 80, 300],
    'Quantity': [5, 3, 8, 4, 2, 10]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
print("Shape:", df.shape, "\n")  # (6, 4)

# 1. Basic Grouping and Simple Aggregation
print("1. Basic Grouping and Simple Aggregation")

# Group by 'Region'
grouped_region = df.groupby('Region')

# Group info
print("Group keys:", list(grouped_region.groups.keys()))  # ['East', 'North', 'South']
print("Group sizes by Region:\n", grouped_region.size())
# East: 2, North: 2, South: 2

# Simple aggregates (applies to all numeric columns)
print("\nMean by Region:\n", grouped_region.mean(numeric_only=True))
# Sales and Quantity means per region

print("Sum of Sales by Region:\n", grouped_region['Sales'].sum())
# East: 380, North: 250, South: 320

print("Count of rows by Region:\n", grouped_region['Sales'].count())
# All 2 per region

print("Min/Max Sales by Region:\n", grouped_region['Sales'].agg(['min', 'max']))
# Multi-function agg

# Get specific group and aggregate on it
east_group = grouped_region.get_group('East')
print("\n'East' group sum:\n", east_group.sum(numeric_only=True), "\n")

# 2. Advanced Aggregation with .agg()
print("2. Advanced Aggregation with .agg()")

# Single function on all numerics
print("Agg 'sum' on numerics:\n", grouped_region.agg('sum', numeric_only=True))

# Multiple functions (list)
multi_agg = grouped_region.agg(['mean', 'sum', 'std'], numeric_only=True)
print("\nMulti-function agg by Region:\n", multi_agg)
# Multi-level columns: mean/sum/std for Sales and Quantity

# Per-column dict: Different functions
agg_dict = grouped_region.agg({
    'Sales': ['mean', 'sum'],
    'Quantity': ['count', 'max']
})
print("\nPer-column agg:\n", agg_dict)

# Flatten multi-level columns (optional)
agg_dict.columns = ['_'.join(col).strip() for col in agg_dict.columns]
print("\nFlattened multi-agg:\n", agg_dict.head())

# as_index=False: Groups as columns, not index
agg_no_index = grouped_region.agg('sum', numeric_only=True).reset_index()
print("\nAgg with as_index=False (reset):\n", agg_no_index)

# 3. Iterating and Custom Aggregation
print("3. Iterating and Custom Aggregation")

# Iterate over groups and apply custom logic
total_revenue = {}
for region, group in grouped_region:
    total_revenue[region] = (group['Sales'] * group['Quantity']).sum()
print("Custom iter agg (total revenue by region):\n", pd.Series(total_revenue))

# Custom function with .agg() (lambda)
custom_agg = grouped_region.agg({
    'Sales': lambda x: x.sum() * 1.1,  # Sum with 10% tax
    'Quantity': 'mean'
})
print("\nCustom lambda agg:\n", custom_agg, "\n")

# 4. Multi-Key Grouping
print("4. Multi-Key Grouping")
multi_grouped = df.groupby(['Region', 'Product'])

# Group info
print("Multi-group keys:", list(multi_grouped.groups.keys()))
# e.g., ('East', 'A'), ('East', 'C'), etc.

# Aggregate on multi-groups
multi_agg = multi_grouped.agg({
    'Sales': 'sum',
    'Quantity': 'mean'
})
print("\nAgg by Region and Product:\n", multi_agg)
# Hierarchical index: Region > Product

# Reset to flat DataFrame
flat_multi = multi_agg.reset_index()
print("\nFlattened multi-agg:\n", flat_multi)

# 5. Handling Edge Cases
print("5. Handling Edge Cases")

# Include NaN groups (if any; add NaN for demo)
df_with_nan = df.copy()
df_with_nan.loc[5, 'Region'] = np.nan  # Make one NaN
grouped_nan = df_with_nan.groupby('Region', dropna=False)
print("Groups including NaN:\n", list(grouped_nan.groups.keys()))  # Includes nan

# Non-numeric agg (e.g., unique products per region)
unique_prods = grouped_region['Product'].agg(lambda x: list(x.unique()))
print("\nUnique Products per Region:\n", unique_prods, "\n")
# North: ['A', 'B'], etc.

# 6. Practice Section - Try These!
print("6. Practice Exercises (Uncomment and Run)")
# Exercise 1: Group by 'Product', median Sales and count
# prod_group = df.groupby('Product')
# print("By Product - median Sales and count:\n", prod_group.agg({
#     'Sales': 'median',
#     'Quantity': 'count'
# }))

# Exercise 2: Multi-group by ['Region', 'Product'], sum Sales, mean Quantity
# multi_g = df.groupby(['Region', 'Product'])
# print("Multi-group agg:\n", multi_g.agg({
#     'Sales': 'sum',
#     'Quantity': 'mean'
# }))

# Exercise 3: Custom agg for total revenue (Sales * Quantity) per Region
# def total_revenue(group):
#     return (group['Sales'] * group['Quantity']).sum()
# print("Custom total revenue by Region:\n", grouped_region.apply(total_revenue))

print("=== End of Demo. Aggregation simplifies complex data! ===")
