# Functions: Definition, Arguments, and Return Values

## Overview
Functions are reusable blocks of code designed to perform a specific task. They help organize code, improve readability, and enable modular programming.

---

## Defining a Function

A function is defined using the `def` keyword followed by a name and parentheses `()` which may include parameters.

### Syntax (Python example)
```python
def function_name(parameters):
    # code block
    return value  # optional
```

---

## Parameters vs Arguments

- **Parameters**: Variables listed in the function definition that act as placeholders.
- **Arguments**: Actual values passed to the function when it is called.

Example:
```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Aayushi")  # "Alice" is an argument
```

---

## Return Statement

- Functions can return a value using the `return` statement.
- Returning a value allows the function to produce output that can be used elsewhere.

---

## Key Points

- Functions encapsulate code for reuse and clarity.
- Parameters define what inputs a function expects.
- Arguments provide actual data to those parameters.
- The `return` statement sends a result back to the caller; if omitted, the function returns `None`.
- Functions can have zero or more parameters.
- Use descriptive function names and parameters for readability.

---

## Practice

1. Define a function that takes two numbers and returns their product.
2. Write a function that checks if a string is a palindrome.
3. Create a function that converts temperatures from Celsius to Fahrenheit.

---

Mastering functions is essential for writing clean, efficient, and maintainable code.
