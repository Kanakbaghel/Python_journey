# 100 Days of Python - Day 47: Writing and Using Python Scripts

## Overview
Welcome to Day 47 of your 100 Days of Python journey! Today, we learn to **write and use Python scripts** that are reusable and runnable from the command line. Scripts are standalone programs you can execute via terminal/command prompt, often with arguments. We'll cover making code modular (reusable functions) and using `if __name__ == "__main__"` to control execution.

This project includes a script for tasks like summing numbers or processing text, demonstrating command-line usage.

## Learning Objectives
By the end of this day, you should understand:
- How to write scripts that run from the command line.
- Using `if __name__ == "__main__"` to separate reusable code from execution.
- Handling command-line arguments with `sys.argv` or `argparse`.
- Making scripts reusable (e.g., importable functions).
- Best practices for script organization and error handling.

## Prerequisites
- Basic Python knowledge (functions, conditionals).
- Python 3.x installed.
- Access to a terminal/command prompt (built-in on most systems).
- No external libraries needed (we use `argparse` from the standard library).

## How to Run the Project
1. **Download or Copy Files**: Save the `day47_scripts.py` file in a folder.
2. **Open a Terminal/Command Prompt**: Navigate to the folder (e.g., `cd path/to/folder`).
3. **Run the Script**: Type commands like:
   - `python day47_scripts.py sum 5 10 15` (sums numbers).
   - `python day47_scripts.py reverse "Hello World"` (reverses text).
   - `python day47_scripts.py --help` (shows help).
4. **View Output**: The script will process arguments and print results. Experiment with different inputs!

## Key Concepts Explained Simply
- **Scripts vs. Modules**: Scripts are executable programs; modules are importable code. Use `if __name__ == "__main__"` to run code only when the file is executed directly (not imported).
- **Command-Line Arguments**: Values passed when running the script (e.g., `python script.py arg1 arg2`). Access via `sys.argv` (basic) or `argparse` (advanced, with help/options).
- **Reusability**: Write functions that can be called from other scripts or imported. Keep execution logic in `if __name__ == "__main__"`.
- **argparse**: A library for parsing arguments, adding descriptions, and handling errors.
- **Running Scripts**: Use `python filename.py` in the terminal. On Windows, ensure Python is in your PATH.

## Examples from the Code
The `day47_scripts.py` script includes these examples:
1. **Reusable Functions**: `sum_numbers()` and `reverse_text()` can be imported or used in the script.
2. **Command-Line Parsing**: Uses `argparse` to define commands and arguments.
3. **Script Execution**: `if __name__ == "__main__"` runs the argument parser and calls functions based on input.
4. **Error Handling**: Checks for valid inputs and shows usage if needed.
5. **Importing**: You can `import day47_scripts` in another file to reuse functions without running the script.

Run the script with arguments to see it in action!

## Tips for Learning
- Always test scripts in the terminal—debugging is easier there.
- Use `argparse` for user-friendly scripts; it's better than raw `sys.argv`.
- Keep scripts modular: Functions first, execution last.
- Add `--help` to your scripts for self-documentation.
- Practice by modifying the script (e.g., add a new command).

## Next Steps
- Day 48 could cover file I/O or data persistence.
- Challenge: Write a script that reads a file and counts words.
- Use scripts for automation, like backups or data processing.

Happy coding! Scripts are powerful for automation—start simple and build up.