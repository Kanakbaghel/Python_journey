# Day 50: Intermediate Pandas - Data Aggregation and Visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(42) 

# --- 1. Data Generation (Simulating a Sales Dataset) ---
DATA_SIZE = 1000

# Create lists/arrays for the DataFrame
customer_ids = np.arange(101, 101 + DATA_SIZE)
regions = np.random.choice(['North', 'South', 'East', 'West'], size=DATA_SIZE, p=[0.25, 0.35, 0.20, 0.20])
sales_amounts = np.random.normal(loc=150.00, scale=50.00, size=DATA_SIZE)
product_categories = np.random.choice(['Electronics', 'Apparel', 'Home Goods', 'Food'], size=DATA_SIZE)

# Create the Pandas DataFrame
sales_df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Region': regions,
    'SalesAmount': sales_amounts,
    'Category': product_categories
})

print("--- 1. Initial Data Snapshot (Head) ---")
print(sales_df.head())
print("\n" + "="*50 + "\n")


# --- 2. Data Filtering and Cleaning ---
# Filter out any sales amounts that are less than $50 (potential noise or errors)
filtered_df = sales_df[sales_df['SalesAmount'] >= 50]

print("--- 2. Filtered Data Info ---")
print(f"Original rows: {len(sales_df)}")
print(f"Filtered rows (Sales >= 50): {len(filtered_df)}")
print("\n" + "="*50 + "\n")


# --- 3. Intermediate Aggregation and Grouping ---
# Task: Find the total and average sales amount for each Region.

# Group by 'Region' and calculate descriptive statistics
regional_summary = filtered_df.groupby('Region').agg(
    TotalSales=('SalesAmount', 'sum'),
    AverageSales=('SalesAmount', 'mean'),
    TransactionCount=('CustomerID', 'count')
).reset_index()

# Round the numerical columns for better presentation
regional_summary['TotalSales'] = regional_summary['TotalSales'].round(2)
regional_summary['AverageSales'] = regional_summary['AverageSales'].round(2)

print("--- 3. Regional Sales Summary (Aggregation) ---")
print(regional_summary.sort_values(by='AverageSales', ascending=False))
print("\n" + "="*50 + "\n")


# --- 4. Basic Data Visualization ---
# Visualize the Average Sales per Region using Matplotlib/Pandas plotting integration

# Select the data for the plot
plot_data = regional_summary.set_index('Region')['AverageSales']

# Create the plot
plt.figure(figsize=(10, 6))
plot_data.plot(kind='bar', color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.title('Average Sales Amount by Region')
plt.ylabel('Average Sales ($)')
plt.xlabel('Region')
plt.xticks(rotation=0) # Keep region names horizontal

# Annotate the bars with the average values
for i, value in enumerate(plot_data):
    plt.text(i, value + 1, f"${value:.2f}", ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

print("--- 4. Visualization ---")
print("A bar chart showing 'Average Sales Amount by Region' has been generated. Close the plot to end the script.")

# Display the plot
plt.show()