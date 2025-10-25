# Day 35: Working with Dates and Times in Pandas
# This script demonstrates handling datetime objects and time-based indexing in Pandas.

import pandas as pd
import numpy as np

# Step 1: Create sample data
# Generate a list of date strings and random values
dates = [
    '2023-01-01 10:00:00', '2023-01-02 11:00:00', '2023-01-03 12:00:00',
    '2023-01-04 13:00:00', '2023-01-05 14:00:00', '2023-02-01 15:00:00',
    '2023-02-02 16:00:00', '2023-02-03 17:00:00', '2023-02-04 18:00:00'
]
values = np.random.randint(1, 10, size=len(dates))  # Random values for demonstration

# Step 2: Convert to DataFrame with datetime index
# Use pd.to_datetime() to parse date strings into datetime objects
df = pd.DataFrame({'value': values}, index=pd.to_datetime(dates))
df.index.name = 'date'  # Name the index for clarity

print("Original DataFrame:")
print(df)
print()

# Step 3: Time-based indexing and slicing
# Pandas allows slicing by date ranges when the index is a DatetimeIndex
# Slice data for January 2023
january_data = df.loc['2023-01-01':'2023-01-31']
print("Data after time-based slicing (January 2023):")
print(january_data)
print()

# Step 4: Resampling for aggregation
# Resample daily data to monthly sums using .resample('M').sum()
# 'M' stands for month-end frequency; you can use 'D' for daily, 'W' for weekly, etc.
monthly_sum = df.resample('M').sum()
print("Monthly Resampled Data (Sum):")
print(monthly_sum)
print()

# Additional demonstration: Filtering specific dates
# For example, get data where the hour is greater than 12
filtered_data = df[df.index.hour > 12]
print("Filtered Data (Hour > 12):")
print(filtered_data)
print()

# Note: This script uses sample data. In real scenarios, load data from CSV/Excel with pd.read_csv(index_col='date', parse_dates=True)
# For timezones, you can add: df.index = df.index.tz_localize('UTC').tz_convert('US/Eastern')
