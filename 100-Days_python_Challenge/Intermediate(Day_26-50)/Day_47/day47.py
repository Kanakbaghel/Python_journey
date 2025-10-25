# Day 47: Writing and Using Python Scripts
# This script demonstrates creating reusable functions and running from the command line.
# It uses argparse for handling arguments and if __name__ == "__main__" for execution control.
# Run with: python day47_scripts.py <command> <args> (e.g., python day47_scripts.py sum 1 2 3)

import argparse  # For parsing command-line arguments
import sys       # For basic argument access (optional, used in comments)

# Example 1: Reusable Functions
# These can be imported into other scripts without running the whole file.
def sum_numbers(*numbers):
    """Sums a list of numbers. Reusable function."""
    try:
        return sum(float(num) for num in numbers)
    except ValueError:
        return "Error: All inputs must be numbers."

def reverse_text(text):
    """Reverses a string. Reusable function."""
    return text[::-1]

# Example 2: Script Execution with if __name__ == "__main__"
# This block only runs when the file is executed directly (not imported).
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="A reusable script for summing numbers or reversing text.")
    parser.add_argument("command", choices=["sum", "reverse"], help="Command to run: 'sum' or 'reverse'")
    parser.add_argument("inputs", nargs="+", help="Inputs: numbers for sum, or a string for reverse")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Example 3: Handling Commands
    if args.command == "sum":
        # Call reusable function
        result = sum_numbers(*args.inputs)
        print(f"Sum of {args.inputs}: {result}")
    elif args.command == "reverse":
        # Join inputs into a string (for multi-word text)
        text = " ".join(args.inputs)
        result = reverse_text(text)
        print(f"Reversed text: {result}")
    
    # Example 4: Error Handling and Help
    # argparse handles invalid commands automatically. For custom errors:
    # If no args, argparse shows help. You can add more checks here.

# Example 5: Importing and Reusability
# In another script, you could do:
# import day47_scripts
# print(day47_scripts.sum_numbers(1, 2, 3))  # Uses function without running script
# This won't execute the if __name__ == "__main__" block.

# Bonus: Basic sys.argv Alternative (commented out, for comparison)
# If not using argparse, access args like this (less user-friendly):
# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Usage: python day47_scripts.py <command> <inputs>")
#         sys.exit(1)
#     command = sys.argv[1]
#     inputs = sys.argv[2:]
#     # Then handle as above...

# Experiment: Run the script with different commands, or import it in a new file!
# Try: python day47_scripts.py sum 10 20 30
