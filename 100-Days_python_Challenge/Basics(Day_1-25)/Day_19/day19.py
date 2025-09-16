## Best Practices for Print Debugging
# Be Descriptive: Include context in your print messages.
print(f"Value of x before loop: {x}")

# Print Variable Types if Needed:
print(f"x = {x} (type: {type(x)})")

# Use Clear Separators or Labels:
print("---- Loop iteration 3 ----")


## Example: Using Print Statements

def factorial(n):
    print(f"Calculating factorial of {n}")
    if n == 0:
        print("Reached base case")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {result}")
        return result

print(factorial(5))

