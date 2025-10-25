# 100 Days of Python - Day 41: Introduction to Regular Expressions in Python

## Overview
Welcome to Day 41 of your 100 Days of Python journey! Today, we explore **Regular Expressions (Regex)**, a powerful tool for pattern matching and text extraction in Python. Regex allows you to search for specific patterns in strings, such as emails, phone numbers, or words, making it useful for tasks like data validation, parsing, and cleaning text.

This project provides a simple introduction with examples. We'll use Python's built-in `re` module to demonstrate basic concepts like matching, searching, and extracting text.

## Learning Objectives
By the end of this day, you should understand:
- What regular expressions are and why they're useful.
- Basic regex patterns (e.g., literals, wildcards, quantifiers).
- How to use Python's `re` module for common tasks.
- Practical applications, like extracting emails from text.

## Prerequisites
- Basic knowledge of Python (variables, loops, strings).
- Python 3.x installed on your system.
- No external libraries needed (we use the built-in `re` module).

## How to Run the Project
1. **Download or Copy Files**: Save the `day41_regex.py` file in a folder on your computer.
2. **Open a Terminal/Command Prompt**: Navigate to the folder containing the file.
3. **Run the Script**: Type `python day41_regex.py` (or `python3 day41_regex.py` on some systems) and press Enter.
4. **View Output**: The script will print examples and results to the console. Experiment by modifying the code!

## Key Concepts Explained Simply
- **Regex Patterns**: These are strings that describe what to search for. For example:
  - `hello` matches the word "hello" exactly.
  - `\d` matches any digit (0-9).
  - `.*` matches any sequence of characters.
- **Python's `re` Module**: Provides functions like:
  - `re.match()`: Checks if the pattern matches at the start of the string.
  - `re.search()`: Finds the first match anywhere in the string.
  - `re.findall()`: Finds all matches and returns them as a list.
- **Common Patterns**:
  - `\w+` : One or more word characters (letters, numbers, underscores).
  - `\d{3}-\d{3}-\d{4}` : A phone number like 123-456-7890.
  - `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` : A basic email pattern.

## Examples from the Code
The `day41_regex.py` script includes these examples:
1. **Matching a Simple Pattern**: Checks if a string starts with "Hello".
2. **Searching for a Word**: Finds "Python" in a sentence.
3. **Extracting Emails**: Pulls email addresses from a block of text.
4. **Finding Phone Numbers**: Extracts phone numbers in a specific format.
5. **Replacing Text**: Swaps words using regex.

Run the script to see the output and try changing the input strings to experiment!

## Tips for Learning
- Regex can be tricky at first—practice with simple patterns.
- Use online tools like Regex101 to test patterns before coding.
- For more depth, check Python's official docs on the `re` module.
- If you get stuck, remember: regex is about describing patterns, not exact matches.

## Next Steps
- Day 42 could build on this by applying regex to real data (e.g., from files or APIs).
- Share your code on GitHub or a forum for feedback!

Happy coding! If you have questions, feel free to ask.