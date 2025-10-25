# Day 40: Histograms, Boxplots, and Heatmaps in Seaborn

Welcome to Day 40 of the 100 Days of Python Challenge\! Today, we dive deeper into the powerful statistical visualization tools provided by **Seaborn**. We'll focus on creating three specific and highly useful plot types to analyze distributions, compare groups, and visualize correlations.

## Goal for Today

The main objective is to gain mastery over key Seaborn functions for statistical analysis:

1.  **Histograms (`sns.histplot`)**: To clearly visualize the frequency distribution of a single variable.
2.  **Boxplots (`sns.boxplot`)**: To compare the statistical distribution (median, quartiles, outliers) of a continuous variable across different categories.
3.  **Heatmaps (`sns.heatmap`)**: To visualize the correlation matrix between multiple numeric variables.

## Key Seaborn Functions for Statistical Analysis

We will focus on these high-impact functions that quickly reveal data insights:

| Function | Plot Type | Statistical Purpose |
| :--- | :--- | :--- |
| **`sns.histplot()`** | Distribution | Shows the shape of the data and identifies central tendency and spread. |
| **`sns.boxplot()`** | Categorical/Distribution | Compares statistical properties (spread, skewness) between groups. |
| **`sns.heatmap()`** | Matrix/Correlation | Visualizes the strength and direction of linear relationships between pairs of variables. |
| **`df.corr()`** | Pandas Utility | Used specifically with `sns.heatmap` to calculate the correlation matrix. |

## Prerequisites

  * Python 3.x installed.
  * The **Pandas** library installed (`pip install pandas`).
  * The **NumPy** library installed (`pip install numpy`).
  * The **Matplotlib** library installed (`pip install matplotlib`).
  * The **Seaborn** library installed (`pip install seaborn`).

## The Python File

The accompanying file, **`day_40_seaborn_adv_plots.py`**, uses a fictional dataset simulating real estate prices and attributes. The script provides step-by-step code and comments for generating all three specified plot types, focusing on clarity and professional presentation.
