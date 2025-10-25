# Day 37: Plotting Line, Bar, and Scatter Plots

## Introduction
Welcome to Day 37 of the 100 Days Python Challenge! Building on Day 36's basics of Matplotlib, today we dive deeper into creating and customizing three fundamental plot types: line plots (for trends), bar plots (for comparisons), and scatter plots (for relationships). We'll emphasize customization to make plots professional and informative, including adding labels, titles, legends, colors, markers, and gridlines.

By the end of this day, you'll be able to:
- Generate line, bar, and scatter plots from data.
- Customize plots extensively for clarity and aesthetics.
- Save and export plots for reports or presentations.
- Combine multiple elements in a single figure (e.g., subplots).

This enhances your data visualization skills, making it easier to communicate insights effectively.

## Objectives
- Create and customize line plots (e.g., time-series trends).
- Create and customize bar plots (e.g., category comparisons).
- Create and customize scatter plots (e.g., variable correlations).
- Apply customizations like labels, titles, legends, colors, and styles.
- Demonstrate saving plots and using subplots for multi-panel figures.

## Prerequisites
- Completion of Day 36 (basic Matplotlib knowledge).
- Basic knowledge of Python (lists, loops).
- Familiarity with Pandas and NumPy (install via `pip install pandas numpy` if needed).
- Matplotlib installation: `pip install matplotlib`.
- Python 3.x environment (e.g., Jupyter Notebook for interactive viewing).

## Key Concepts
1. **Plot Types**:
   - **Line Plot**: Use `plt.plot()` for continuous data trends.
   - **Bar Plot**: Use `plt.bar()` for categorical comparisons.
   - **Scatter Plot**: Use `plt.scatter()` for bivariate relationships.
2. **Customizations**:
   - **Labels and Titles**: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`.
   - **Legends**: `plt.legend()` to identify plot elements.
   - **Colors and Styles**: Parameters like `color`, `marker`, `linestyle`, `alpha`.
   - **Grid and Layout**: `plt.grid()`, `plt.tight_layout()`.
   - **Subplots**: `plt.subplot()` for multiple plots in one figure.
3. **Saving Plots**: `plt.savefig()` to export as PNG, PDF, etc.

## Code Structure
The provided Python script (`day37.py`) includes:
- Importing libraries (Matplotlib, Pandas, NumPy).
- Creating sample data for each plot type.
- Generating customized line, bar, and scatter plots.
- Demonstrating subplots and saving all plots.
- Printing confirmation messages.

## Usage
1. Download or copy the `day37.py` script.
2. Run it in your Python environment: