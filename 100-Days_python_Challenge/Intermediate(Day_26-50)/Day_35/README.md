# Day 35: Working with Dates and Times in Pandas

## Introduction
Welcome to Day 35 of the 100 Days Python Challenge! Today, we dive into handling dates and times using the Pandas library in Python. Pandas provides powerful tools for working with datetime data, making it easy to parse, manipulate, and analyze time-series data. This includes creating datetime objects, converting strings to dates, performing time-based indexing, and resampling data over time intervals.

By the end of this day, you'll understand how to:
- Convert strings and other formats into Pandas datetime objects.
- Work with DatetimeIndex for efficient time-based operations.
- Perform slicing and filtering based on dates.
- Resample data to aggregate over time periods (e.g., daily to monthly summaries).

This is essential for data analysis tasks involving time-series data, such as stock prices, weather logs, or user activity tracking.

## Objectives
- Learn to handle datetime objects in Pandas.
- Perform time-based indexing and slicing.
- Demonstrate resampling for time-series aggregation.
- Apply these concepts to a practical example with sample data.

## Prerequisites
- Basic knowledge of Python (variables, loops, functions).
- Familiarity with Pandas (install via `pip install pandas` if needed).
- Optional: NumPy for array operations (install via `pip install numpy`).
- Python 3.x environment (e.g., Jupyter Notebook or a script editor).

## Key Concepts
1. **Datetime Objects**: Pandas uses `pd.to_datetime()` to convert strings, lists, or other formats into datetime objects.
2. **DatetimeIndex**: A special index type for time-series data, enabling fast lookups and operations.
3. **Time-Based Indexing**: Slice data using date ranges (e.g., `df.loc['2023-01-01':'2023-01-31']`).
4. **Resampling**: Aggregate data over time intervals using `.resample()` (e.g., convert daily data to monthly averages).

## Code Structure
The provided Python script (`day35.py`) includes:
- Importing necessary libraries.
- Creating sample time-series data.
- Demonstrating datetime conversion and indexing.
- Performing time-based slicing and resampling.
- Printing results for verification.

## Usage
1. Download or copy the `day35.py` script.
2. Run it in your Python environment: