# Python Syntax, Variables, and Data Types

This guide introduces you to the fundamental building blocks of Python programming: its syntax rules, variables, and basic data types. Understanding these concepts is essential for writing clear and effective Python code.

---

## Table of Contents

- [1. Python Syntax Rules](#1-python-syntax-rules)
- [2. Variables in Python](#2-variables-in-python)
- [3. Basic Data Types](#3-basic-data-types)
  - [3.1 Integer (`int`)](#31-integer-int)
  - [3.2 Floating Point (`float`)](#32-floating-point-float)
  - [3.3 String (`str`)](#33-string-str)
  - [3.4 Boolean (`bool`)](#34-boolean-bool)

---

## 1. Python Syntax Rules

Python syntax is designed to be readable and straightforward. Here are some key rules:

- **Indentation is significant:**  
  Python uses indentation (usually 4 spaces) to define blocks of code instead of braces `{}`.  
  Example:

  ```python
  if True:
      print("This is indented")
  ```

- **Case sensitivity:**  
  Variable names and keywords are case-sensitive. For example, `Variable` and `variable` are different.

- **Comments:**  
  Use `#` for single-line comments.

  ```python
  # This is a comment
  ```

- **Statements:**  
  Each statement typically goes on its own line. Use a semicolon `;` to separate multiple statements on the same line (not common practice).

- **No need for explicit variable declarations:**  
  Variables are created when you assign a value to them.

---

## 2. Variables in Python

Variables are containers for storing data values. You do not need to declare their type explicitly.

### Rules for variable names:

- Must start with a letter (a-z, A-Z) or underscore `_`.
- Can contain letters, digits (0-9), and underscores.
- Cannot be a Python keyword (e.g., `if`, `for`, `while`).
- Case-sensitive (`myVar` and `myvar` are different).

### Assigning values:

```python
x = 10
name = "Alice"
is_active = True
```

---

## 3. Basic Data Types

Python has several built-in data types. Here are the most common basic types:

### 3.1 Integer (`int`)

- Represents whole numbers (positive, negative, or zero).
- No limit on size (only limited by available memory).

### 3.2 Floating Point (`float`)

- Represents decimal numbers (numbers with fractional parts).

### 3.3 String (`str`)

- Represents sequences of characters (text).
- Can be enclosed in single quotes `'...'`, double quotes `"..."`, or triple quotes `'''...'''` / `"""..."""` for multi-line strings.

### 3.4 Boolean (`bool`)

- Represents truth values: `True` or `False`.
- Often used in conditions and control flow.

---

## Summary

- Python syntax relies on indentation and is case-sensitive.
- Variables are dynamically typed and created upon assignment.
- Basic data types include:
  - `int` for whole numbers,
  - `float` for decimal numbers,
  - `str` for text,
  - `bool` for truth values.

Mastering these basics will help you write clean and effective Python code.

---

*Happy coding!* 
