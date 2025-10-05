# Day 26: Introduction to NumPy Arrays and Operations
# Import NumPy with common alias
import numpy as np

print("=== Day 26: NumPy Arrays and Operations Demo ===\n")

# 1. Creating Arrays
print("1. Creating Arrays")
# 1D array from a list
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1d)
print("Shape:", arr1d.shape)
print("Data type:", arr1d.dtype)
print("Dimensions:", arr1d.ndim, "\n")

# 2D array (matrix) from nested lists
arr2d = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2d)
print("Shape:", arr2d.shape, "\n")

# Other creation methods
zeros = np.zeros((2, 2))  # 2x2 array of zeros
print("Zeros array:\n", zeros)

ones = np.ones(3)  # 1D array of ones
print("Ones array:", ones, "\n")

arange = np.arange(0, 10, 2)  # Like range: start, stop, step
print("Arange (0 to 10, step 2):", arange, "\n")

random_arr = np.random.rand(2, 3)  # 2x3 random array (0 to 1)
print("Random 2x3 array:\n", random_arr, "\n")

# 2. Indexing and Slicing
print("2. Indexing and Slicing")
print("1D slice [1:4]:", arr1d[1:4])  # Elements 1 to 3 (0-based)

print("2D element [0,1]:", arr2d[0, 1])  # Row 0, column 1 = 2

print("2D row slice (row 0):", arr2d[0, :])  # Entire row 0
print("2D column slice (col 0):", arr2d[:, 0])  # Entire column 0
print("2D subarray (rows 0-1, cols 0-1):\n", arr2d[0:2, 0:2], "\n")  # Whole array in this case

# 3. Basic Array Operations
print("3. Basic Operations")
# Element-wise arithmetic (works on arrays of same shape)
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
print("Array A:", arr_a)
print("Array B:", arr_b)
print("Element-wise addition:", arr_a + arr_b)  # [5 7 9]
print("Element-wise multiplication:", arr_a * arr_b, "\n")  # [4 10 18]

# Broadcasting: Add scalar to array (expands scalar to match shape)
print("Broadcasting: Add 10 to arr_a:", arr_a + 10, "\n")  # [11 12 13]

# 2D example with broadcasting
arr2d_b = np.array([[1, 2], [3, 4]])
add_row = np.array([10, 20])  # 1D array broadcasts to each row
print("2D Broadcasting (add row vector):\n", arr2d_b + add_row, "\n")
# Output:
# [[11 22]
#  [13 24]]

# Universal functions (ufuncs) - apply to entire array
print("Sine of arr_a:", np.sin(arr_a), "\n")  # Trigonometric function

# Aggregation functions
data = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Standard deviation:", np.std(data), "\n")

# Reshaping arrays (total elements must match)
flat = np.arange(12)  # [0 1 2 ... 11]
reshaped = flat.reshape(3, 4)  # 3x4 matrix
print("Reshaped (3x4):\n", reshaped, "\n")

# Transpose (swap rows/columns)
print("Transpose of reshaped:\n", reshaped.T, "\n")  # 4x3 matrix

print("=== End of Demo. NumPy makes numerical ops efficient! ===")
