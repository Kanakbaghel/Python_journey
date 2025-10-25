# Day 39: Introduction to Seaborn for Statistical Plots

Welcome to Day 39 of the 100 Days of Python Challenge\! Having mastered the basics of Pandas and the customization tools of Matplotlib, we now introduce **Seaborn**, a powerful Python library specifically designed for creating **informative and attractive statistical graphics**.

Seaborn is built on top of Matplotlib and integrates beautifully with Pandas DataFrames, offering high-level commands to generate complex plots easily.

## Goal for Today

The primary goal is to understand the Seaborn workflow and use its core functions to generate insightful visualizations quickly:

1.  **Generate** a **Distribution Plot** (`histplot`) to visualize a single variable's frequency.
2.  **Create** a **Relationship Plot** (`scatterplot`) to examine the correlation between two variables.
3.  **Construct** a **Categorical Plot** (`boxplot`) to compare distributions across different groups.
4.  **Utilize** Seaborn's default themes and color palettes for enhanced aesthetics.

## Key Seaborn Concepts and Functions

Seaborn operates on the principle of mapping data variables to visual elements (like color, size, and position).

| Function | Plot Type | Purpose |
| :--- | :--- | :--- |
| **`sns.histplot()`** | Univariate | Visualizes the distribution of a single variable using bars (histogram) or a curve (KDE). |
| **`sns.scatterplot()`** | Bivariate | Visualizes the relationship between two continuous variables. |
| **`sns.boxplot()`** | Categorical | Shows the distribution (median, quartiles, outliers) of a quantitative variable across categories. |
| **`sns.set_theme()`** | Style | Sets the default aesthetic parameters for all subsequent plots (e.g., color palette, font size). |
| **`data=` Parameter** | Data Input | A consistent parameter in almost all Seaborn functions, specifying the Pandas DataFrame. |

## Prerequisites

  * Python 3.x installed.
  * The **Pandas** library installed (`pip install pandas`).
  * The **Matplotlib** library installed (`pip install matplotlib`).
  * The **Seaborn** library installed (`pip install seaborn`).

## The Python File

The accompanying file, **`day_39_seaborn_intro.py`**, uses a sample dataset (fictional product metrics) to demonstrate the power and simplicity of Seaborn by creating three distinct, publication-quality statistical plots.
