# Day 49: Exception Handling in Python
# This script demonstrates handling exceptions with try/except, raising custom errors, and best practices.
# It integrates with logging for better error tracking.

import logging  # From Day 48: For logging errors

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Example 1: Basic try/except Block
# Handles a common error like division by zero.
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        logging.error("Attempted division by zero.")
        return None

print("Example 1 - Basic try/except:")
safe_divide(10, 2)  # Works
safe_divide(10, 0)  # Triggers exception

# Example 2: Multiple except Blocks
# Catches different types of exceptions separately.
def process_input(value):
    try:
        num = int(value)  # Could raise ValueError
        result = 100 / num  # Could raise ZeroDivisionError
        print(f"Processed: {result}")
    except ValueError:
        print("Error: Invalid input - must be a number.")
        logging.warning("ValueError: Non-numeric input.")
    except ZeroDivisionError:
        print("Error: Cannot process zero.")
        logging.error("ZeroDivisionError: Division by zero.")

print("\nExample 2 - Multiple except Blocks:")
process_input("5")   # Works
process_input("abc") # ValueError
process_input("0")   # ZeroDivisionError

# Example 3: else and finally Clauses
# else: Runs if no exception. finally: Always runs (for cleanup).
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        logging.error(f"FileNotFoundError: {filename}")
        return None
    else:
        print("File read successfully.")
        return content
    finally:
        print("Cleanup: File operation complete.")  # Always runs

print("\nExample 3 - else and finally:")
read_file("nonexistent.txt")  # Error
read_file(__file__)           # Success (reads this script)

# Example 4: Raising Custom Exceptions
# Define and raise your own exceptions for specific cases.
class NegativeNumberError(Exception):
    pass  # Custom exception class

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Number must be positive!")  # Raise custom error
    return num * 2

try:
    result = check_positive(-5)
except NegativeNumberError as e:
    print(f"Custom Error: {e}")
    logging.warning(f"NegativeNumberError: {e}")

print("\nExample 4 - Raising Custom Exceptions:")
try:
    result = check_positive(5)  # Works
    print(f"Result: {result}")
except NegativeNumberError as e:
    print(f"Error: {e}")

# Example 5: Handling User Input with Exceptions
# Simulates real-world input handling (e.g., in a loop for retries).
def get_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")
            logging.info("Retrying input due to ValueError.")

print("\nExample 5 - User Input Handling:")
# Uncomment to test interactively: number = get_number(); print(f"You entered: {number}")

# Experiment: Add try/except to your own functions or raise a new custom exception!
# Try causing errors on purpose to see handling.
