# Day 28: NumPy Broadcasting and Vectorization
# Import NumPy and time for speed demo
import numpy as np
import time

print("=== Day 28: NumPy Broadcasting and Vectorization Demo ===\n")

# 1. Vectorization Basics
print("1. Vectorization Basics")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 4, 6, 8, 10])

# Element-wise operations (vectorized - no loops!)
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Vectorized Addition:", arr1 + arr2)  # [3 6 9 12 15]
print("Vectorized Multiplication:", arr1 * arr2)  # [2 8 18 32 50]
print("Vectorized Power:", arr1 ** 2, "\n")  # [1 4 9 16 25]

# Universal functions (ufuncs) - vectorized and fast
print("Vectorized Sin:", np.sin(arr1))  # Sine of each element
print("Vectorized Exp:", np.exp(arr2[:3]), "\n")  # Exp of first 3: ~[7.39 54.6 403.43]

# 2. Broadcasting Examples
print("2. Broadcasting Examples")

# Scalar broadcasting (shape () to match array)
scalar = 3
print("Scalar + Array:", arr1 + scalar)  # [4 5 6 7 8] - scalar expands to each element
print("Array * Scalar:", arr1 * scalar, "\n")  # [3 6 9 12 15]

# 1D + 1D (same shape - direct element-wise)
print("1D + 1D (same shape):", np.array([1, 2, 3]) + np.array([4, 5, 6]), "\n")  # [5 7 9]

# 1D + 2D (broadcast 1D across rows)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
row_vector = np.array([1, 2, 3])  # Shape (3,)
print("2D Array:\n", arr2d)
print("Row vector (1D):", row_vector)
print("1D + 2D Broadcasting (adds to each row):\n", arr2d + row_vector)
# Output:
# [[ 2  4  6]
#  [ 5  7  9]
#  [ 8 10 12]]
print("\nShapes: 2D=(3,3), 1D=(3,) → 1D pads to (1,3), broadcasts to (3,3)")

# Column vector broadcasting (add to each column)
col_vector = np.array([[10], [20], [30]])  # Shape (3,1)
print("Column vector (3x1):\n", col_vector)
print("2D + Column Broadcasting (adds to each column):\n", arr2d + col_vector)
# Output:
# [[11 12 13]
#  [24 25 26]
#  [37 38 39]]
print("\nShapes: 2D=(3,3), Col=(3,1) → Col broadcasts to (3,3)")

# Incompatible shapes (will raise ValueError)
try:
    bad_add = arr2d + np.array([1, 2])  # (3,3) + (2,) → Incompatible
except ValueError as e:
    print("Incompatible Example Error:", str(e)[:50] + "...", "\n")

# Using np.newaxis to enable broadcasting
arr1d_newaxis = arr1[:, np.newaxis]  # Shape (5,1) - column vector
print("1D as column (with np.newaxis): Shape", arr1d_newaxis.shape)
print("Broadcast example with newaxis:\n", arr1d_newaxis + np.array([10, 20, 30, 40, 50]))
# Adds element-wise after broadcasting (5,1) + (5,) → (5,5)

# Check broadcast shapes
print("Broadcast shapes check:", np.broadcast_shapes((3, 4), (4,)))  # ((3, 4), (1, 4)) → OK
print("Incompatible check:", np.broadcast_shapes((3, 4), (5,)), "→ Error expected\n")

# 3. Vectorization vs. Loops - Speed Demo
print("3. Vectorization vs. Loops (Speed Comparison)")
large_arr1 = np.random.rand(1000000)  # 1M elements
large_arr2 = np.random.rand(1000000)

# Loop version (slow Python)
start = time.time()
result_loop = np.zeros_like(large_arr1)
for i in range(len(large_arr1)):
    result_loop[i] = large_arr1[i] * large_arr2[i]
loop_time = time.time() - start

# Vectorized version (fast NumPy)
start = time.time()
result_vectorized = large_arr1 * large_arr2
vectorized_time = time.time() - start

print(f"Loop Time: {loop_time:.4f}s | Vectorized Time: {vectorized_time:.6f}s")
print(f"Speedup: {loop_time / vectorized_time:.1f}x faster with vectorization!")
print("First 5 elements match:", np.allclose(result_loop[:5], result_vectorized[:5]), "\n")

# Vectorized ufunc on large array
start = time.time()
np.sin(large_arr1)  # Just compute - don't store if not needed
ufunc_time = time.time() - start
print(f"Vectorized np.sin() on 1M elements: {ufunc_time:.6f}s\n")

# 4. Practice Section - Try These!
print("4. Practice Exercises (Uncomment and Run)")
# Exercise 1: 4x3 array + 1D length 3
# mat = np.ones((4,3))
# vec = np.array([1,2,3])
# print("4x3 + 1D(3) broadcast:\n", mat + vec)  # Broadcasts to each row

# Exercise 2: Time sin on 1M vs loop
# def python_sin_loop(arr):
#     return np.array([np.sin(x) for x in arr])  # Still uses np.sin, but list comp overhead
# start_loop = time.time()
# python_sin_loop(large_arr1)
# print("Python loop sin time:", time.time() - start_loop)

# Exercise 3: Row normalization (broadcast subtract mean)
# row_means = np.mean(arr2d, axis=1, keepdims=True)  # Shape (3,1)
# normalized = arr2d - row_means
# print("Row-normalized 2D:\n", normalized)  # Each row mean=0

print("=== End of Demo. Broadcasting + Vectorization = NumPy Magic! ===")
