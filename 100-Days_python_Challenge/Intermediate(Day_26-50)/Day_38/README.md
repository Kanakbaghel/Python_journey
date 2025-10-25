# Day 38: Customizing Plots (Labels, Titles, Legends)

Welcome to Day 38 of the 100 Days of Python Challenge\! Today, we transition from just *generating* plots to **customizing** them. A plot that lacks clear labels, a descriptive title, or a helpful legend is often useless, no matter how accurate the data is.

This day focuses on using **Matplotlib** (specifically the `pyplot` interface, usually imported as `plt`), which underlies the plotting functionality in Pandas, to refine the aesthetics and readability of our visualizations.

## Goal for Today

The main goal is to learn how to significantly improve plot readability and aesthetics by implementing:

1.  **Descriptive Titles** for the overall plot.
2.  **Clear Axis Labels** to define the data being measured.
3.  **Informative Legends** to differentiate multiple data series.
4.  **Stylistic Elements** like gridlines and custom colors.

## Key Matplotlib Methods

We will be using the following essential methods from the `matplotlib.pyplot` module:

| Method | Purpose |
| :--- | :--- |
| **`plt.title()`** | Sets the main title of the plot. |
| **`plt.xlabel()`** | Sets the label for the x-axis. |
| **`plt.ylabel()`** | Sets the label for the y-axis. |
| **`plt.legend()`** | Displays the legend using labels defined in the `plot()` call. |
| **`plt.grid()`** | Adds gridlines for easier data point reading. |
| **`plt.style.use()`** | Changes the overall aesthetic theme of the plot. |

## Prerequisites

  * Python 3.x installed.
  * The **Pandas** library installed (`pip install pandas`).
  * The **Matplotlib** library installed (`pip install matplotlib`).

## The Python File

The accompanying file, **`day_38_custom_plots.py`**, contains a complete, commented script that demonstrates how to create a basic plot and then step-by-step apply all the customization techniques to make it presentation-ready.
