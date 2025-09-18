### Recursive Implementation

def factorial(n):
    if n == 0:            # Base case
        return 1
    else:                 # Recursive case
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


def fibonacci(n):
    if n == 0:            # Base case 1
        return 0
    elif n == 1:          # Base case 2
        return 1
    else:                 # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # Output: 13

