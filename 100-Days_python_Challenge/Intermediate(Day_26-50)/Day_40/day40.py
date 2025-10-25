import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Data Preparation: Creating a Fictional Real Estate Dataset ---
# Simulating a dataset with features useful for correlation and comparison.
np.random.seed(42)

n_rows = 200
data = {
    'Price_K': np.random.normal(loc=400, scale=150, size=n_rows).round(0), # Price in thousands
    'Size_sqft': np.random.normal(loc=1800, scale=400, size=n_rows).round(0),
    'Beds': np.random.randint(2, 6, size=n_rows),
    'Baths': np.random.randint(1, 4, size=n_rows),
    'Age_Years': np.random.randint(1, 40, size=n_rows),
    'City': np.random.choice(['Suburbia', 'Downtown', 'Rural'], size=n_rows)
}
df = pd.DataFrame(data)

# Introduce some correlation
df['Price_K'] = df['Price_K'] + (df['Size_sqft'] * 0.1) + (df['Beds'] * 5)
df['Price_K'] = df['Price_K'].round(0)

print("--- 1. Sample DataFrame Head ---")
print(df.head())
print("-" * 50)


# ----------------------------------------------------------------------
# --- 2. Setting the Seaborn Aesthetic Theme ---
# Ensures all plots look professional and consistent.
sns.set_theme(style="whitegrid", palette="deep")


# ----------------------------------------------------------------------
# --- 3. Plot 1: Histogram (Visualizing Distribution) ---
# Goal: Analyze the distribution of 'Price_K' (our primary variable).
# ----------------------------------------------------------------------

plt.figure(figsize=(9, 6))
sns.histplot(
    data=df,
    x='Price_K',
    kde=True,  # Add a density line to show the smooth distribution
    bins=20,   # Specify the number of bins
    color='skyblue',
    edgecolor='black'
)
plt.title('Distribution of Property Prices (K)', fontsize=15, fontweight='bold')
plt.xlabel('Price in Thousands ($K)')
plt.ylabel('Count of Properties')
plt.show()


# ----------------------------------------------------------------------
# --- 4. Plot 2: Boxplot (Comparing Distributions Across Categories) ---
# Goal: Compare property prices based on the 'City' category.
# ----------------------------------------------------------------------

plt.figure(figsize=(8, 6))
sns.boxplot(
    data=df,
    x='City',
    y='Price_K',
    notch=False, # Standard boxplot without notches
    linewidth=1.5,
    hue='City', # Use the 'City' column to apply different colors
    legend=False # Hide the redundant legend
)
plt.title('Property Price Distribution by City Type', fontsize=15, fontweight='bold')
plt.xlabel('City Type')
plt.ylabel('Price in Thousands ($K)')
plt.show()


# ----------------------------------------------------------------------
# --- 5. Plot 3: Heatmap (Visualizing Correlation) ---
# Goal: Show the linear relationship between all numeric variables.
# ----------------------------------------------------------------------

# A. Calculate the Correlation Matrix using Pandas
# Select only numeric columns and calculate the Pearson correlation coefficient.
corr_matrix = df[['Price_K', 'Size_sqft', 'Beds', 'Baths', 'Age_Years']].corr()

plt.figure(figsize=(8, 7))
sns.heatmap(
    corr_matrix,
    annot=True,         # Show the correlation values on the map
    fmt=".2f",          # Format the annotations to two decimal places
    cmap='coolwarm',    # Color map: 'coolwarm' is excellent for showing positive/negative values
    linewidths=.5,      # Add lines between cells for clarity
    cbar_kws={'label': 'Correlation Coefficient'}
)
plt.title('Correlation Matrix of Real Estate Attributes', fontsize=15, fontweight='bold')
plt.show()

print("-" * 50)
print("Script finished. Three advanced statistical plots generated using Seaborn.")