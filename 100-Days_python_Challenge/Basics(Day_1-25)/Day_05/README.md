# Conditional Statements: `if`, `elif`, and `else`

## Overview
Conditional statements allow programs to make decisions and execute different code blocks based on boolean conditions. The primary constructs are:

- **`if`**: Executes a block if a condition is true.
- **`elif`** (else if): Checks additional conditions if previous `if` or `elif` conditions are false.
- **`else`**: Executes a block if all preceding conditions are false.

---

## Syntax (Python example)

```python
if condition1:
    # code block executed if condition1 is True
elif condition2:
    # code block executed if condition1 is False and condition2 is True
else:
    # code block executed if all above conditions are False
```

---

## How It Works

- The program evaluates conditions in order.
- The first condition that evaluates to `True` triggers its block.
- Remaining conditions are skipped once a match is found.
- If no conditions are true, the `else` block runs (if present).

---

## Key Points

- Conditions must evaluate to boolean values (`True` or `False`).
- Use `elif` to check multiple exclusive conditions.
- `else` is optional but useful as a fallback.
- Indentation defines code blocks in Python.

---

## Practice

1. Write a program that checks if a number is positive, negative, or zero.
2. Create a grading system that assigns letter grades based on score ranges.
3. Implement a simple login check that verifies username and password.

---

Mastering conditional statements enables your programs to respond dynamically to different inputs and states.
