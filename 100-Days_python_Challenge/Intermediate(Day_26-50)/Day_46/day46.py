# Day 46: Decorators and Generators
# This script demonstrates decorators (function modifiers) and generators (lazy value producers).
# Examples show practical uses like timing and generating sequences.

import time  # For timing in decorators
import functools  # For preserving function metadata in decorators

# Example 1: Basic Decorator - A Timer Decorator
# Decorators modify functions. This one times how long a function takes to run.
def timer(func):
    @functools.wraps(func)  # Preserves func's name/docstring
    def wrapper(*args, **kwargs):
        start = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end = time.time()  # Record end time
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result  # Return the original result
    return wrapper

@timer  # Apply the decorator with @
def slow_function():
    time.sleep(1)  # Simulate a slow task
    return "Done!"

print("Example 1 - Timer Decorator:")
result = slow_function()  # Calls decorated function
print("Result:", result)

# Example 2: Decorator with Arguments - A Logging Decorator
# This decorator logs function calls with arguments.
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logger  # Apply the decorator
def add_numbers(a, b):
    return a + b

print("\nExample 2 - Logging Decorator:")
sum_result = add_numbers(5, 3)  # Logs the call and result

# Example 3: Simple Generator - Generating Squares
# Generators use 'yield' to produce values one at a time.
def generate_squares(n):
    for i in range(n):
        yield i ** 2  # Yield pauses and returns value; resumes on next call

print("\nExample 3 - Simple Generator (Squares):")
squares = generate_squares(5)  # Creates a generator object
for square in squares:  # Iterate to get values
    print(square, end=" ")  # Prints: 0 1 4 9 16

# Example 4: Infinite Generator - Fibonacci Sequence
# Generators can be infinite; use with care (e.g., break loops).
def fibonacci():
    a, b = 0, 1
    while True:
        yield a  # Yield current value
        a, b = b, a + b  # Update for next

print("\n\nExample 4 - Infinite Generator (Fibonacci):")
fib_gen = fibonacci()
for _ in range(10):  # Generate first 10 numbers
    print(next(fib_gen), end=" ")  # next() gets the next yielded value

# Example 5: Using Generators for Memory Efficiency
# Compare a list (loads all at once) vs. generator (lazy).
def large_list(n):  # Regular function returning a list
    return [i for i in range(n)]

def large_generator(n):  # Generator version
    for i in range(n):
        yield i

print("\n\nExample 5 - Memory Efficiency:")
n = 1000000  # Large number
# list_version = large_list(n)  # Would create a huge list in memory
gen_version = large_generator(n)  # Generator: no big memory use
print("Generator created. First 5 values:")
for i in range(5):
    print(next(gen_version), end=" ")  # Only computes as needed

# Experiment: Create your own decorator (e.g., for counting calls) or generator (e.g., evens)!
# Try decorating a generator function.
