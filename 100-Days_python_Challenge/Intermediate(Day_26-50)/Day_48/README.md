# 100 Days of Python - Day 49: Exception Handling in Python

## Overview
Welcome to Day 49 of your 100 Days of Python journey! Today, we explore **exception handling** in Python, a way to manage errors and unexpected events without crashing your program. Exceptions are like "emergency signals" for issues like division by zero or file not found. We'll use `try`, `except`, `else`, and `finally` to catch and handle them, making code robust.

This project demonstrates handling common exceptions, raising custom ones, and integrating with logging (from Day 48).

## Learning Objectives
By the end of this day, you should understand:
- What exceptions are and why they're important.
- Using `try/except` blocks to catch errors.
- Raising custom exceptions with `raise`.
- The `else` and `finally` clauses for advanced handling.
- Best practices: When to handle vs. let errors propagate.

## Prerequisites
- Basic Python knowledge (functions, conditionals).
- Completion of Day 48 (logging) for integration examples.
- Python 3.x installed.
- No external libraries needed.

## How to Run the Project
1. **Download or Copy Files**: Save the `day49_exceptions.py` file in a folder.
2. **Open a Terminal/Command Prompt**: Navigate to the folder.
3. **Run the Script**: Type `python day49_exceptions.py` and press Enter.
4. **View Output**: The script will simulate errors, handle them, and show results. It may prompt for input—try entering invalid data!
5. **Experiment**: Modify the code to trigger different exceptions.

## Key Concepts Explained Simply
- **Exceptions**: Errors that occur during execution (e.g., `ZeroDivisionError`, `FileNotFoundError`). They "raise" and can be "caught."
- **try/except**: `try` runs risky code; `except` catches specific exceptions and handles them.
- **else**: Runs if no exception in `try`.
- **finally**: Always runs, for cleanup (e.g., closing files).
- **raise**: Manually trigger an exception (e.g., for custom errors).
- **Built-in Exceptions**: Common ones like `ValueError` (bad input), `TypeError` (wrong type).
- **Why Handle?**: Prevents crashes; allows graceful recovery (e.g., ask for input again).

## Examples from the Code
The `day49_exceptions.py` script includes these examples:
1. **Basic try/except**: Handles division by zero.
2. **Multiple except Blocks**: Catches different exceptions separately.
3. **else and finally**: Shows code that runs conditionally or always.
4. **Raising Exceptions**: Creates and raises a custom exception.
5. **Integration with Logging**: Logs errors instead of just printing.

Run the script to see error handling in action!

## Tips for Learning
- Don't catch all exceptions with bare `except`—be specific.
- Use `finally` for resources like files/networks.
- Combine with logging for better debugging.
- Test by intentionally causing errors (e.g., divide by zero).
- Handle user input carefully—assume it's invalid.

## Next Steps
- Day 50 could cover file I/O or data structures.
- Challenge: Add exception handling to a previous script.
- Apply to real code, like web apps or data processing.

Happy coding! Exception handling makes programs resilient—practice catching errors!