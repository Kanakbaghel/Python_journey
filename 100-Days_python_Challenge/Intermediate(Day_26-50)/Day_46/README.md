# 100 Days of Python - Day 46: Decorators and Generators

## Overview
Welcome to Day 46 of your 100 Days of Python journey! Today, we explore **decorators** and **generators**, advanced function features that make your code more powerful and efficient. **Decorators** are like wrappers that modify or enhance functions without changing their code. **Generators** are special functions that produce values one at a time (lazily), saving memory for large data.

This project shows how to use decorators to add logging or timing, and generators for sequences like numbers or data streams.

## Learning Objectives
By the end of this day, you should understand:
- What decorators are and how to create/use them.
- How generators work with `yield` for lazy evaluation.
- Practical uses, like timing functions or generating infinite sequences.
- When to use these features for cleaner, efficient code.

## Prerequisites
- Basic Python knowledge (functions, loops).
- Completion of earlier days (e.g., functions from Day 1-10).
- Python 3.x installed.
- No external libraries needed.

## How to Run the Project
1. **Download or Copy Files**: Save the `day46_decorators_generators.py` file in a folder.
2. **Open a Terminal/Command Prompt**: Navigate to the folder.
3. **Run the Script**: Type `python day46_decorators_generators.py` and press Enter.
4. **View Output**: The script will demonstrate decorators and generators. Experiment by modifying the code!

## Key Concepts Explained Simply
- **Decorators**: Functions that take another function as input and return a modified version. Use `@decorator_name` above a function to apply it. They add behavior like logging or timing without rewriting code.
- **Generators**: Functions that use `yield` instead of `return`. They pause and resume, producing values on demand. Great for large lists or infinite sequences—memory-efficient.
- **yield vs. return**: `return` ends the function; `yield` pauses it, allowing iteration.
- **Common Uses**: Decorators for cross-cutting concerns (e.g., authentication); generators for data processing (e.g., reading files line-by-line).

## Examples from the Code
The `day46_decorators_generators.py` script includes these examples:
1. **Basic Decorator**: A timer decorator that measures function execution time.
2. **Decorator with Arguments**: A logging decorator that prints function calls.
3. **Simple Generator**: Generates squares of numbers up to a limit.
4. **Infinite Generator**: Produces an endless Fibonacci sequence.
5. **Using Generators in Loops**: Demonstrates lazy evaluation and memory savings.

Run the script to see timing, logging, and generated sequences!

## Tips for Learning
- Decorators can be tricky—start with simple ones and build up.
- Generators are lazy: They don't compute everything at once.
- Use `@functools.wraps` in decorators to preserve function metadata.
- Test generators with `next()` or loops; they're iterators.
- Practice by decorating existing functions or creating custom generators.

## Next Steps
- Day 47 could cover context managers or async programming.
- Challenge: Write a decorator for caching results or a generator for prime numbers.
- Apply to real code, like timing API calls or generating reports.

Happy coding! Decorators and generators are advanced but rewarding—experiment freely.