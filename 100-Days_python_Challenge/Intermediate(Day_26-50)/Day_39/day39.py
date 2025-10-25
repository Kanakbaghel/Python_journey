import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Data Preparation: Creating a Fictional Dataset ---
# We use a DataFrame that mimics product metrics (e.g., website traffic and sales).
np.random.seed(42)  # For reproducible results

data = {
    'Category': np.random.choice(['Electronics', 'Books', 'Apparel'], size=100),
    'Monthly_Traffic': np.random.normal(loc=10000, scale=3000, size=100).round(0),
    'Conversion_Rate': np.random.beta(a=2, b=50, size=100) * 100, # Rate between 0 and 100
    'Average_Order_Value': np.random.randint(50, 300, size=100)
}
df = pd.DataFrame(data)

# Introduce correlation for the scatter plot
df['Monthly_Traffic'] = df['Monthly_Traffic'] + (df['Average_Order_Value'] * 5)

print("--- 1. Sample DataFrame Head (First 5 Rows) ---")
print(df.head())
print("-" * 50)


# ----------------------------------------------------------------------
# --- 2. Setting the Seaborn Aesthetic Theme ---
# ----------------------------------------------------------------------
# Seaborn themes instantly improve plot aesthetics without manual tuning.
sns.set_theme(style="whitegrid", palette="viridis")
# style options: "darkgrid", "whitegrid", "dark", "white", "ticks"
# palette options: "viridis", "pastel", "deep", "colorblind"


# ----------------------------------------------------------------------
# --- 3. Plot 1: Univariate Distribution Plot (Histplot) ---
# Goal: Visualize the frequency distribution of 'Conversion_Rate'.
# ----------------------------------------------------------------------

plt.figure(figsize=(8, 5))
# The 'data' parameter is the DataFrame, 'x' is the column name.
sns.histplot(
    data=df,
    x='Conversion_Rate',
    kde=True,  # Add a Kernel Density Estimate line for smoothing
    bins=15,   # Number of bins/buckets for the histogram
    edgecolor='black'
)
plt.title('Distribution of Conversion Rates', fontsize=14, fontweight='bold')
plt.xlabel('Conversion Rate (%)')
plt.ylabel('Frequency (Count)')
plt.show()


# ----------------------------------------------------------------------
# --- 4. Plot 2: Bivariate Relationship Plot (Scatterplot) ---
# Goal: Examine the relationship between traffic and sales value.
# ----------------------------------------------------------------------

plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x='Monthly_Traffic',
    y='Average_Order_Value',
    hue='Category',  # Map a categorical variable to color
    size='Conversion_Rate', # Map a third variable to marker size
    alpha=0.7 # Transparency
)
plt.title('Monthly Traffic vs. Average Order Value, by Category', fontsize=14, fontweight='bold')
plt.xlabel('Monthly Traffic (Log Scale Recommended)')
plt.ylabel('Average Order Value ($)')
# The legend is automatically added and labeled by 'hue' and 'size'.
plt.legend(title='Category', loc='best')
plt.show()


# ----------------------------------------------------------------------
# --- 5. Plot 3: Categorical Plot (Boxplot) ---
# Goal: Compare the distribution of Order Value across different categories.
# ----------------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.boxplot(
    data=df,
    x='Category',
    y='Average_Order_Value',
    notch=True, # Shows confidence intervals around the median
    linewidth=1.5
)
plt.title('Average Order Value Distribution per Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Product Category')
plt.ylabel('Average Order Value ($)')
plt.show()

print("-" * 50)
print("Script finished. Three statistical plots generated using Seaborn.")