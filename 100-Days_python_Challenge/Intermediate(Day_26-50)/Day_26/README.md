# 100 Days of Code Challenge - Day 26: Introduction to NumPy Arrays and Operations

## Overview
Today, I dove into **NumPy** (Numerical Python), a powerful library for scientific computing in Python. NumPy provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them efficiently. It's the foundation for many data science and machine learning libraries like Pandas, SciPy, and TensorFlow.

Key focus: Understanding NumPy arrays (ndarrays) and basic operations. Arrays are faster and more memory-efficient than Python lists for numerical data, and they enable vectorized operations (performing math on entire arrays without loops).

### What I Learned Today
- **Importing NumPy**: Use `import numpy as np` (common alias).
- **Creating Arrays**:
  - From lists: `np.array([1, 2, 3])`
  - Zeros/ones: `np.zeros(5)` or `np.ones((2, 3))` (shape as tuple for multi-dim).
  - Range: `np.arange(0, 10, 2)` (start, stop, step).
  - Random: `np.random.rand(3, 3)` for uniform random values.
- **Array Attributes**:
  - Shape: `arr.shape` (e.g., `(3, 4)` for a 3x4 matrix).
  - Data type: `arr.dtype` (e.g., `int32`, `float64`).
  - Dimension: `arr.ndim` (scalar, 1D, 2D, etc.).
- **Indexing and Slicing**:
  - 1D: Like lists, e.g., `arr[0]` or `arr[1:4]`.
  - 2D: `arr[row, col]` or `arr[0:2, 1:3]` (row slices, column slices).
- **Basic Operations**:
  - Element-wise arithmetic: `arr + 5`, `arr * arr2` (broadcasting aligns shapes).
  - Universal functions (ufuncs): `np.add(arr1, arr2)`, `np.sin(arr)`.
  - Aggregation: `np.sum(arr)`, `np.mean(arr)`, `np.max(arr)`.
  - Reshaping: `arr.reshape(3, 4)` (must match total elements).
- **Broadcasting**: NumPy automatically expands arrays of different shapes for operations (e.g., adding a scalar to an array).
- **Why NumPy?** It avoids slow Python loops for math-heavy tasks, making code faster and more readable.

Challenges encountered: Understanding broadcasting rules (e.g., shapes must be compatible). Pro tip: Always check `arr.shape` after operations!

### Code Example
Run the Python script `day26_numpy_intro.py` to see demonstrations. It prints outputs for each section.

### How to Run
1. Ensure NumPy is installed: `pip install numpy`.
2. Save the Python code to `day26_numpy_intro.py`.
3. Run: `python day26_numpy_intro.py`.

### Output Preview
The script will output arrays, operations, and results like:

1D Array: [1 2 3 4 5] Shape: (5,) 2D Array: [[0. 0.] [0. 0.]] Element-wise Addition: [[2. 3.] [4. 5.]] Mean of array: 3.0

