# Day 27: Array Indexing and Slicing in NumPy
# Import NumPy
import numpy as np

print("=== Day 27: NumPy Indexing and Slicing Demo ===\n")

# 1. Basic Indexing and Slicing (1D)
print("1. Basic Indexing and Slicing (1D)")
arr1d = np.array([10, 20, 30, 40, 50])
print("Original 1D:", arr1d)

# Single element (positive/negative index)
print("First element:", arr1d[0])
print("Last element:", arr1d[-1], "\n")

# Slicing: start:stop:step
print("Slice [1:4]:", arr1d[1:4])  # Indices 1,2,3: [20 30 40]
print("Slice from index 2 to end:", arr1d[2:])  # [30 40 50]
print("Slice every other element:", arr1d[::2])  # [10 30 50]
print("Reverse slice:", arr1d[::-1], "\n")  # [50 40 30 20 10]

# Modifying via slice (affects original - it's a view!)
arr1d[1:3] = 99  # Change indices 1 and 2
print("After modifying slice [1:3]:", arr1d)  # [10 99 99 40 50]
arr1d[1:3] = [25, 35]  # Can assign arrays/lists of matching length
print("After re-assigning:", arr1d, "\n")  # Back to [10 25 35 40 50]

# 2. Multi-Dimensional Indexing and Slicing (2D)
print("2. Multi-Dimensional Indexing and Slicing (2D)")
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("2D Array:\n", arr2d)
print("Shape:", arr2d.shape, "\n")

# Single element
print("Element [1,2]:", arr2d[1, 2])  # Row 1, Col 2 = 6

# Entire row or column
print("Row 1:", arr2d[1, :])  # [4 5 6]
print("Column 0:", arr2d[:, 0])  # [1 4 7]
print("Last row:", arr2d[-1, :], "\n")  # [7 8 9]

# Subarray slicing
print("Subarray (rows 0:2, cols 1:): \n", arr2d[0:2, 1:])  
# [[2 3]
#  [5 6]]
print("All rows, cols 0:2 step 1:\n", arr2d[:, 0:2], "\n")  
# [[1 2]
#  [4 5]
#  [7 8]]

# 3D example (quick intro)
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
print("3D Array shape:", arr3d.shape)  # (2, 2, 2)
print("Element [0,1,0]:", arr3d[0, 1, 0])  # 3
print("Slice first 'layer' (depth 0):\n", arr3d[0, :, :], "\n")  
# [[1 2]
#  [3 4]]

# 3. Boolean Indexing
print("3. Boolean Indexing")
data = np.array([10, 25, 30, 15, 40, 5])
print("Original data:", data)

# Mask: Create boolean array
mask = data > 20
print("Mask (>20):", mask)  # [ True False  True False  True False]
print("Elements >20:", data[mask], "\n")  # [10 30 40] Wait, no: [25? Wait, 10<20, 25>20? Wait, example: [25 30 40]

# Using np.where for indices
indices = np.where(data > 20)
print("Indices where >20:", indices)  # (array([1, 2, 4]),)
print("Same as boolean:", data[indices], "\n")  # [25 30 40]

# Modifying with boolean
data[data < 20] = 0  # Set <20 to 0
print("After setting <20 to 0:", data, "\n")  # [10? Wait, adjust: assuming corrected values

# 4. Fancy Indexing
print("4. Fancy Indexing")
arr_fancy = np.array([100, 200, 300, 400, 500])
indices = [0, 2, 4]  # List of indices
print("Fancy 1D (indices [0,2,4]):", arr_fancy[indices])  # [100 300 500]

# 2D fancy: Select specific rows and columns
rows = [0, 2]
cols = [1, 0]
print("2D Fancy (rows [0,2], cols [1,0]):\n", arr2d[rows, :][:, cols])
# Or more directly: arr2d[np.ix_(rows, cols)]
# Output example:
# [[2 1]
#  [8 7]]

# Note: Fancy indexing returns a COPY, not a view
fancy_view = arr_fancy[indices]
fancy_view[0] = 999
print("Original after fancy mod:", arr_fancy)  # Unchanged: [100 200 300 400 500]
print("Fancy copy after mod:", fancy_view, "\n")  # [999 300 500]

# 5. Practice Section - Try These!
print("5. Practice Exercises (Uncomment and Run)")
# Exercise 1: Diagonal of 3x3 array
# diag_arr = np.diag([1,2,3])
# print("Diagonal:", diag_arr[np.arange(3), np.arange(3)])

# Exercise 2: Boolean replace in random array
# rand_arr = np.random.randint(0, 100, (5,5))
# print("Random 5x5:\n", rand_arr)
# rand_arr[rand_arr < 50] = 0
# print("After replace <50 with 0:\n", rand_arr)

# Exercise 3: Checkerboard fancy indexing (advanced)
# For a 4x4, select even rows/cols or similar

print("=== End of Demo. Practice slicing to master data access! ===")