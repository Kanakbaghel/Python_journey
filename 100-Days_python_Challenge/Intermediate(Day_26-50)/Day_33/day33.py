# Day 33: Merging, Joining, and Concatenating DataFrames
# Import Pandas and NumPy
import pandas as pd
import numpy as np

print("=== Day 33: Pandas Combining DataFrames Demo ===\n")

# Sample DataFrames
students = pd.DataFrame({
    'Student_ID': [1, 2, 3],
    'Age': [22, 21, 23],
    'Grade': [85.0, 92.0, np.nan]
})
print("Students DF:\n", students)

enrollments = pd.DataFrame({
    'Student_ID': [1, 2, 2, 4],
    'Course': ['Math', 'CS', 'Physics', 'Math'],
    'Credits': [3, 4, 3, 3]
})
print("\nEnrollments DF:\n", enrollments, "\n")

# Additional DF for concat demo
more_students = pd.DataFrame({
    'Student_ID': [4],
    'Age': [20],
    'Grade': [78.0]
})
print("More Students DF:\n", more_students, "\n")

# 1. Concatenation
print("1. Concatenation with pd.concat()")

# Vertical concat (stack rows, axis=0)
concat_vertical = pd.concat([students, more_students], ignore_index=True)
print("Concat vertical (students + more students):\n", concat_vertical)
print("Shape:", concat_vertical.shape, "\n")  # (4, 3)

# Horizontal concat (side-by-side, axis=1) - assumes matching rows
# Add a dummy column DF for demo
dummy_cols = pd.DataFrame({'Status': ['Active', 'Active', 'Inactive']}, index=[0,1,2])
concat_horizontal = pd.concat([students, dummy_cols], axis=1)
print("Concat horizontal (add Status column):\n", concat_horizontal, "\n")

# Concat with keys (multi-index)
concat_keys = pd.concat([students, more_students], keys=['Original', 'Additional'])
print("Concat with keys (hierarchical index):\n", concat_keys, "\n")

# Inner join on columns (only common columns)
# For demo: Concat with mismatched columns
mismatched = pd.DataFrame({'Extra': [10, 20]})
concat_inner = pd.concat([students.iloc[:2], mismatched], axis=1, join='inner')
print("Concat inner (common columns only):\n", concat_inner, "\n")  # Only Student_ID, Age, Grade for first 2

# 2. Merging
print("2. Merging with pd.merge()")

# Inner merge (default: intersection on common keys)
merge_inner = pd.merge(students, enrollments, on='Student_ID', how='inner')
print("Inner Merge on Student_ID:\n", merge_inner)
# Students 1 and 2 (with duplicate for student 2's two courses)
print("Shape:", merge_inner.shape, "\n")  # (3, 5)

# Left merge (all from left, matching from right)
merge_left = pd.merge(students, enrollments, on='Student_ID', how='left')
print("Left Merge (all students, optional courses):\n", merge_left)
# Student 3 gets NaNs for Course/Credits

# Outer merge (union: all from both)
merge_outer = pd.merge(students, more_students, on='Student_ID', how='outer', suffixes=('_students', '_more'))
print("Outer Merge (students + more, with suffixes):\n", merge_outer)
# Includes student 4; suffixes for duplicate columns

# Right merge
merge_right = pd.merge(students, enrollments, on='Student_ID', how='right')
print("Right Merge (all enrollments, optional students):\n", merge_right)
# Student 4 gets NaNs for Age/Grade

# Merge on different column names
# For demo: Assume 'ID' in one
enroll_copy = enrollments.copy()
enroll_copy.rename(columns={'Student_ID': 'ID'}, inplace=True)
merge_diff_keys = pd.merge(students, enroll_copy, left_on='Student_ID', right_on='ID', how='inner')
print("Merge on different keys (Student_ID == ID):\n", merge_diff_keys.head(), "\n")

# Multi-key merge
# Add another key for demo
students['Year'] = 2023
enrollments['Year'] = [2023, 2023, 2023, 2024]
merge_multi = pd.merge(students, enrollments, on=['Student_ID', 'Year'], how='inner')
print("Multi-key merge (Student_ID and Year):\n", merge_multi, "\n")

# Indicator for join source
merge_ind = pd.merge(students, enrollments, on='Student_ID', how='outer', indicator=True)
print("Merge with indicator (shows source):\n", merge_ind['_merge'].value_counts())
# both: 3, left_only: 1 (student 3), right_only: 1 (student 4)

# 3. Joining
print("3. Joining with df.join()")

# Set index for join demo
students_indexed = students.set_index('Student_ID')
enroll_indexed = enrollments.set_index('Student_ID')

# Default: Left join on index
join_default = students_indexed.join(enroll_indexed, how='left')
print("Index-based Join (left):\n", join_default)
# Same as left merge; student 3 gets NaNs

# Right join
join_right = students_indexed.join(enroll_indexed, how='right')
print("Index-based Right Join:\n", join_right)
# Includes student 4; duplicates for student 2

# Join on non-index (but join is index-focused; use merge for columns)
# For multi-DataFrames: df1.join([df2, df3])

# 4. Practice Section - Try These!
print("4. Practice Exercises (Uncomment and Run)")
# Exercise 1: Horizontal concat of students and a new 'Department' DF
# depts = pd.DataFrame({'Department': ['CS', 'Math', 'Physics']})
# horiz_concat = pd.concat([students, depts], axis=1)
# print("Horizontal concat with depts:\n", horiz_concat)

# Exercise 2: Outer merge students and enrollments; count NaNs
# outer_full = pd.merge(students, enrollments, on='Student_ID', how='outer')
# print("Outer merge:\n", outer_full)
# print("NaN counts:\n", outer_full.isna().sum())

# Exercise 3: Join on custom indices (e.g., set 'Age' as index)
# students_age_idx = students.set_index('Age')
# enroll_age_idx = enrollments.assign(Age=[22, 21, 21, 20]).set_index('Age')
# custom_join = students_age_idx.join(enroll_age_idx, how='right', lsuffix='_stu')
# print("Custom index join:\n", custom_join)

print("=== End of Demo. Combining DataFrames builds richer datasets! ===")
