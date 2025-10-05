# 100 Days of Code Challenge - Day 27: Array Indexing and Slicing in NumPy

## Overview
Building on Day 26, today I practiced **advanced indexing and slicing** in NumPy arrays. Indexing lets you access specific elements or subsets efficiently, while slicing creates views (not copies) of arrays for memory efficiency. This is crucial for data analysis, as it avoids slow loops and enables vectorized operations.

Key focus: Efficiently accessing/slicing 1D and multi-dimensional arrays. NumPy's indexing is powerful—beyond Python lists—with support for booleans, integers, and even arrays as indices.

### What I Learned Today
- **Basic Indexing**:
  - 1D: `arr[0]` (single element), `arr[-1]` (last element).
  - 2D+: `arr[row, col]` (e.g., `arr[0, 1]` for row 0, col 1).
- **Slicing**:
  - Syntax: `arr[start:stop:step]` (start defaults to 0, stop to end, step to 1).
  - Multi-dim: `arr[rows_slice, cols_slice]` (e.g., `arr[0:2, 1:]` for first two rows, columns from 1 onward).
  - Negative indices/steps: `arr[::-1]` (reverse array).
  - Views vs. Copies: Slicing returns a view (changes affect original); use `arr.copy()` for a copy.
- **Boolean Indexing**:
  - Use a boolean array/mask: `arr[arr > 5]` (selects elements > 5).
  - Great for filtering: `arr[np.where(arr % 2 == 0)]` (even numbers).
- **Fancy Indexing**:
  - Use lists/arrays of indices: `arr[[0, 2, 4]]` (select rows 0, 2, 4).
  - Multi-dim: `arr[[0,1], [2,0]]` (row 0 col 2, row 1 col 0).
  - Returns a copy, not a view.
- **Advanced Tips**:
  - `np.ix_` for combining fancy indices in multi-dim.
  - `np.where(condition)`: Returns indices where condition is True.
  - Efficiency: Indexing is O(1) for access; slicing is O(n) but fast for large arrays.
- **Common Pitfalls**: Modifying slices can alter the original (views). Always check with `arr.base is None` (None means copy).

Challenges: Wrapping my head around fancy indexing order (it's not broadcasting). Pro tip: Use `print(arr.shape)` after slicing to verify dimensions!

### Code Example
The script `day27_numpy_indexing.py` demonstrates all concepts with 1D/2D/3D arrays. It includes a practice section—try modifying it!

### How to Run
1. Ensure NumPy is installed: `pip install numpy`.
2. Save the Python code to `day27_numpy_indexing.py`.
3. Run: `python day27_numpy_indexing.py`.

### Output Preview
The script outputs examples like:
Original 1D: [10 20 30 40 50] Slice [1:4]: [20 30 40] Boolean (>30): [40 50] Fancy (indices [0,2,4]): [10 30 50]

2D Array: [[1 2 3] [4 5 6] [7 8 9]] Row 1: [4 5 6] Subarray (rows 0:2, cols 1:): [[2 3] [5 6]]