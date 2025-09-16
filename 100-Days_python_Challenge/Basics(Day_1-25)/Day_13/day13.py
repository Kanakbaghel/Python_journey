## Examples

### 1. Creating a list of squares
squares = [x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

### 2. Filtering with a condition
evens = [x for x in range(20) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

### 3. Applying functions or methods
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# Output: ['HELLO', 'WORLD', 'PYTHON']


### 4. Nested list comprehensions
matrix = [[j for j in range(3)] for i in range(3)]
# Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]