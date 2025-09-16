## Lambda
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

## Functional Programming Tools

### 1. `map()`
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16]

### 2. `filter()`
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]

### 3. `reduce()`
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

## Combining Lambda with map/filter/reduce
#Lambda functions are ideal for quick, inline function definitions when using these tools:
# Double even numbers and sum them
numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda acc, x: acc + x,
    map(
        lambda x: x * 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)  # Output: 24 (2*2 + 4*2 + 6*2 = 4 + 8 + 12)

