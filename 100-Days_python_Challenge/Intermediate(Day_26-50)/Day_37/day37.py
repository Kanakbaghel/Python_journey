# Day 37: Plotting Line, Bar, and Scatter Plots
# This script demonstrates creating and customizing line, bar, and scatter plots with labels, titles, and legends.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 1: Set up Matplotlib style for consistency
plt.style.use('seaborn-v0_8')  # Modern style; fallback to 'default' if not available

# Step 2: Sample data for line plot (e.g., monthly sales trend)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_2023 = [100, 120, 150, 130, 180, 200]
sales_2024 = [110, 130, 160, 140, 190, 210]

# Step 3: Create customized line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales_2023, marker='o', linestyle='-', color='blue', linewidth=2, label='2023 Sales')
plt.plot(months, sales_2024, marker='s', linestyle='--', color='green', linewidth=2, label='2024 Sales')
plt.title('Monthly Sales Comparison (Line Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig('custom_line_plot.png')
print("Custom line plot saved as 'custom_line_plot.png'")
plt.close()

# Step 4: Sample data for bar plot (e.g., product sales by category)
categories = ['Electronics', 'Clothing', 'Books', 'Home']
sales_values = [500, 300, 200, 400]

# Step 5: Create customized bar plot
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, sales_values, color=['red', 'blue', 'green', 'orange'], width=0.6, edgecolor='black')
plt.title('Sales by Category (Bar Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(axis='y', alpha=0.5)  # Grid only on y-axis
# Add value labels on bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'{bar.get_height()}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('custom_bar_plot.png')
print("Custom bar plot saved as 'custom_bar_plot.png'")
plt.close()

# Step 6: Sample data for scatter plot (e.g., height vs. weight with size as age)
np.random.seed(42)
heights = np.random.normal(170, 10, 50)
weights = heights * 0.5 + np.random.normal(0, 5, 50)
ages = np.random.randint(20, 60, 50)  # Age as size

# Step 7: Create customized scatter plot
plt.figure(figsize=(8, 5))
scatter = plt.scatter(heights, weights, s=ages*2, c=ages, cmap='viridis', alpha=0.7, edgecolors='black')
plt.title('Height vs. Weight (Scatter Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Height (cm)', fontsize=12)
plt.ylabel('Weight (kg)', fontsize=12)
plt.colorbar(scatter, label='Age')  # Colorbar for age
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig('custom_scatter_plot.png')
print("Custom scatter plot saved as 'custom_scatter_plot.png'")
plt.close()

# Step 8: Create a subplot figure combining all three plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Line plot in subplot 1
axes[0].plot(months, sales_2023, marker='o', color='blue', label='2023')
axes[0].plot(months, sales_2024, marker='s', color='green', label='2024')
axes[0].set_title('Line Plot')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Sales')
axes[0].legend()
axes[0].grid(True)

# Bar plot in subplot 2
axes[1].bar(categories, sales_values, color=['red', 'blue', 'green', 'orange'])
axes[1].set_title('Bar Plot')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Sales')
axes[1].grid(axis='y')

# Scatter plot in subplot 3
axes[2].scatter(heights, weights, s=ages, c=ages, cmap='viridis', alpha=0.7)
axes[2].set_title('Scatter Plot')
axes[2].set_xlabel('Height')
axes[2].set_ylabel('Weight')

plt.tight_layout()
plt.savefig('combined_plots.png')
print("Subplot figure saved as 'combined_plots.png'")
plt.close()

# Note: In interactive environments, add plt.show() after each plt.savefig() to display.
# For real data, load from files: df = pd.read_csv('data.csv'), then plot df.columns.
# Explore more: Add plt.ylim() for axis limits or plt.annotate() for text annotations.
