import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Data Preparation ---
# Create a sample time series DataFrame for demonstration
dates = pd.date_range('2024-01-01', periods=10)
data = {
    'Sales_A': np.random.randint(100, 200, 10) + np.arange(10) * 5,
    'Sales_B': np.random.randint(80, 150, 10) + np.arange(10) * 8
}
df = pd.DataFrame(data, index=dates)

print("--- 1. Sample Data Head ---")
print(df.head())


# ----------------------------------------------------------------------
# --- 2. Basic Plot (Uncustomized) ---
# ----------------------------------------------------------------------

# Set a style for a cleaner look (optional, but good practice)
plt.style.use('ggplot')

# Create a figure and an axes object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot both series. Note the 'label' argument is CRITICAL for the legend.
df['Sales_A'].plot(
    ax=ax,
    kind='line',
    label='Product A Sales',
    color='darkblue',
    marker='o'
)

df['Sales_B'].plot(
    ax=ax,
    kind='line',
    label='Product B Sales',
    color='darkred',
    marker='x'
)

# ----------------------------------------------------------------------
# --- 3. Customizing the Plot (The Goal for Day 38) ---
# ----------------------------------------------------------------------

# A. Adding a Descriptive Title
plt.title("Monthly Sales Comparison: Product A vs. Product B", fontsize=16, fontweight='bold')

# B. Adding Clear Axis Labels
plt.xlabel("Observation Date", fontsize=12, color='gray')
plt.ylabel("Total Revenue (in thousands $)", fontsize=12)

# C. Adding and Customizing the Legend
# The legend uses the 'label' arguments from the plot() calls in Step 2.
plt.legend(
    title="Product Line",
    loc='upper left', # Places the legend in the top-left corner
    frameon=True,     # Draws a frame around the legend
    shadow=True
)

# D. Adding Gridlines for Readability
plt.grid(True, linestyle='--', alpha=0.7)

# E. Customizing Axis Ticks (Optional, but good for date data)
# Rotate x-axis ticks to prevent overlap
plt.xticks(rotation=45, ha='right')

# Add a text annotation to highlight a specific point (e.g., peak sales)
peak_date = df.index[-1]
peak_sale = df['Sales_A'].iloc[-1]
plt.annotate(
    f'Peak Sale: ${peak_sale}',
    xy=(peak_date, peak_sale),
    xytext=(peak_date - pd.Timedelta(days=5), peak_sale - 50),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
    fontsize=10
)


# ----------------------------------------------------------------------
# --- 4. Final Display ---
# ----------------------------------------------------------------------

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Display the customized plot
print("\n--- Displaying the Customized Plot. Close the window to continue. ---")
plt.show()

print("Script finished. Check the generated plot for all the customizations!")