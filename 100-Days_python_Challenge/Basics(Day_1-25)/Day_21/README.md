# Day 21: Working with JSON and CSV Files

Welcome to Day 21! Today, we focus on handling two of the most common data interchange formats: **JSON** and **CSV**. Python’s standard library provides robust modules to read, write, and manipulate these formats efficiently.

---

## Overview

- **JSON (JavaScript Object Notation)**: A lightweight, human-readable format for structured data.
- **CSV (Comma-Separated Values)**: A simple tabular data format widely used for spreadsheets and databases.

---

## 1. Working with JSON Files

The `json` module allows you to easily encode and decode JSON data.

### Key Functions

- `json.load(file_obj)`: Parse JSON data from a file object into Python objects.
- `json.loads(string)`: Parse JSON data from a string.
- `json.dump(obj, file_obj)`: Serialize Python objects as JSON and write to a file.
- `json.dumps(obj)`: Serialize Python objects as a JSON-formatted string.

---

## 2. Working with CSV Files

The `csv` module provides functionality to read from and write to CSV files, supporting different delimiters and quoting styles.

### Key Classes and Functions

- `csv.reader(file_obj)`: Reads CSV data row by row as lists.
- `csv.writer(file_obj)`: Writes rows (lists) to a CSV file.
- `csv.DictReader(file_obj)`: Reads CSV data as dictionaries (keys from header row).
- `csv.DictWriter(file_obj, fieldnames)`: Writes dictionaries to CSV with specified fieldnames.

---

## Summary

- Use the **`json`** module to work with JSON data: easy serialization and deserialization between Python objects and JSON.
- Use the **`csv`** module to handle CSV files: read/write tabular data efficiently.
- Both modules are part of Python’s standard library — no external dependencies needed.
- Mastering these formats is essential for data exchange, storage, and interoperability.

---

## Further Reading

- [Python `json` module documentation](https://docs.python.org/3/library/json.html)
- [Python `csv` module documentation](https://docs.python.org/3/library/csv.html)

---

Happy data handling! 📊📁
