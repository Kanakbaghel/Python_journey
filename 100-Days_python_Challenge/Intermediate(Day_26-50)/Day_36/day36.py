# Day 36: Introduction to Matplotlib for Data Visualization
# This script demonstrates creating basic plots: line plots and scatter plots using Matplotlib.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 1: Set up Matplotlib style (optional, for better visuals)
plt.style.use('default')  # You can change to 'seaborn' or others

# Step 2: Create sample data for line plot (e.g., time-series data like daily sales)
dates = pd.date_range('2023-01-01', periods=10, freq='D')  # 10 days of dates
sales = np.random.randint(50, 200, size=10)  # Random sales values
df_line = pd.DataFrame({'date': dates, 'sales': sales})

# Step 3: Create a line plot
plt.figure(figsize=(8, 5))  # Set figure size
plt.plot(df_line['date'], df_line['sales'], marker='o', linestyle='-', color='blue', label='Sales')
plt.title('Daily Sales Trend (Line Plot)')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust layout to prevent clipping
plt.savefig('line_plot.png')  # Save the plot as PNG
print("Line plot saved as 'line_plot.png'")
plt.close()  # Close the figure to free memory

# Step 4: Create sample data for scatter plot (e.g., height vs. weight)
np.random.seed(42)  # For reproducible random data
heights = np.random.normal(170, 10, 50)  # Random heights (cm)
weights = heights * 0.5 + np.random.normal(0, 5, 50)  # Weights correlated with heights (kg)

# Step 5: Create a scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(heights, weights, color='red', alpha=0.7, s=50, label='Data Points')  # s for size, alpha for transparency
plt.title('Height vs. Weight (Scatter Plot)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('scatter_plot.png')  # Save the plot as PNG
print("Scatter plot saved as 'scatter_plot.png'")
plt.close()

# Note: In an interactive environment (e.g., Jupyter), add plt.show() after each plot to display inline.
# For real data, load from CSV: df = pd.read_csv('data.csv'), then plot df['column1'] vs df['column2'].
# To customize further, explore plt.colorbar() for scatter plots or plt.fill_between() for line plots.
