# 100 Days of Code Challenge - Day 28: NumPy Broadcasting and Vectorization

## Overview
Today, I explored **broadcasting** and **vectorization** in NumPy—core features that enable efficient, loop-free operations on arrays. Broadcasting automatically "expands" arrays of compatible shapes for element-wise operations, while vectorization applies functions to entire arrays in compiled C code (via ufuncs). This is why NumPy is 10-100x faster than pure Python for math-heavy tasks.

Key focus: Understanding broadcasting rules and using vectorized ops for speed. No more manual loops for additions or multiplications!

### What I Learned Today
- **Vectorization Basics**:
  - Element-wise ops: `arr1 + arr2`, `arr * 3` apply to every element without loops.
  - Universal Functions (ufuncs): `np.add()`, `np.sin()`, `np.exp()`—all vectorized and broadcast-aware.
  - Benefits: Readable code, faster execution (uses optimized C backend).
- **Broadcasting Rules**:
  - Compare shapes from right to left (trailing dimensions).
  - Compatible if: Dimensions match, OR one is 1 (broadcasts along that axis).
  - Examples:
    - Scalar (shape `()`) + array: Scalar broadcasts to array shape.
    - 1D (e.g., `(3,)`) + 2D (e.g., `(3, 4)`): 1D becomes `(1, 3)` then `(3, 3)`, broadcasts to `(3, 4)`.
    - Incompatible: `(3, 4)` + `(5,)` → Error (no match or 1).
  - Prepending 1s: NumPy pads shorter shapes with 1s on the left (e.g., `(3,)` becomes `(1, 3)` for 2D).
- **Advanced Broadcasting**:
  - Multi-dim: Works across axes (e.g., add row vector to each row of matrix).
  - `np.newaxis` or `None`: Reshape to add dimensions (e.g., `arr[:, np.newaxis]` makes column vector).
  - Check compatibility: Use `np.broadcast_shapes(shape1, shape2)`.
- **Vectorization vs. Loops**:
  - Vectorized: `result = arr1 * arr2` (fast).
  - Loop: Slow for large arrays (Python overhead).
  - Pro tip: Always vectorize first; use `@np.vectorize` only if needed for custom functions.
- **Common Pitfalls**: Shape mismatches raise `ValueError`. Debug with `print(arr1.shape, arr2.shape)`.

Challenges: Visualizing broadcasting for non-matching dims. Pro tip: Use `np.broadcast_to(arr, new_shape)` to see the "expanded" array!

### Code Example
The script `day28_numpy_broadcasting.py` shows broadcasting in action, vectorized ops, and a speed comparison (vectorized vs. loop on a large array).

### How to Run
1. Ensure NumPy is installed: `pip install numpy`.
2. Save the Python code to `day28_numpy_broadcasting.py`.
3. Run: `python day28_numpy_broadcasting.py`.

### Output Preview
The script outputs examples like:
Scalar + Array: [5 6 7 8] 1D + 2D Broadcasting: [[ 5 6 7] [ 9 10 11] [13 14 15]] Vectorized Multiplication: [ 2 8 18 32 50] Loop Time: 0.0012s | Vectorized Time: 0.00001s (100x faster!)