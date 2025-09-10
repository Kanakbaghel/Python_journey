# Python Basics: Operators and Expressions

This guide covers the fundamental operators in Python, including arithmetic, comparison, logical, and assignment operators. It also explains how to write expressions combining these operators.

---

## Table of Contents

- [Arithmetic Operators](#arithmetic-operators)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [Assignment Operators](#assignment-operators)
- [Combining Operators in Expressions](#combining-operators-in-expressions)
- [Examples](#examples)

---

## Arithmetic Operators

Arithmetic operators perform mathematical operations on numeric values.

| Operator | Description       | Example       | Result  |
|----------|-------------------|---------------|---------|
| `+`      | Addition          | `5 + 3`       | `8`     |
| `-`      | Subtraction       | `5 - 3`       | `2`     |
| `*`      | Multiplication    | `5 * 3`       | `15`    |
| `/`      | Division (float)  | `5 / 2`       | `2.5`   |
| `//`     | Floor division    | `5 // 2`      | `2`     |
| `%`      | Modulus (remainder) | `5 % 2`     | `1`     |
| `**`     | Exponentiation    | `5 ** 2`      | `25`    |

---

## Comparison Operators

Comparison operators compare two values and return a Boolean (`True` or `False`).

| Operator | Description          | Example       | Result  |
|----------|----------------------|---------------|---------|
| `==`     | Equal to             | `5 == 3`      | `False` |
| `!=`     | Not equal to         | `5 != 3`      | `True`  |
| `>`      | Greater than         | `5 > 3`       | `True`  |
| `<`      | Less than            | `5 < 3`       | `False` |
| `>=`     | Greater than or equal| `5 >= 5`      | `True`  |
| `<=`     | Less than or equal   | `5 <= 3`      | `False` |

---

## Logical Operators

Logical operators combine Boolean expressions.

| Operator | Description       | Example               | Result  |
|----------|-------------------|-----------------------|---------|
| `and`    | Logical AND       | `(5 > 3) and (2 < 4)` | `True`  |
| `or`     | Logical OR        | `(5 > 3) or (2 > 4)`  | `True`  |
| `not`    | Logical NOT       | `not (5 > 3)`         | `False` |

---

## Assignment Operators

Assignment operators assign values to variables, optionally performing an operation first.

| Operator | Description           | Example          | Equivalent To      |
|----------|-----------------------|------------------|--------------------|
| `=`      | Assign                | `x = 5`          | `x = 5`            |
| `+=`     | Add and assign        | `x += 3`         | `x = x + 3`        |
| `-=`     | Subtract and assign   | `x -= 2`         | `x = x - 2`        |
| `*=`     | Multiply and assign   | `x *= 4`         | `x = x * 4`        |
| `/=`     | Divide and assign     | `x /= 2`         | `x = x / 2`        |
| `//=`    | Floor divide and assign | `x //= 3`      | `x = x // 3`       |
| `%=`     | Modulus and assign    | `x %= 2`         | `x = x % 2`        |
| `**=`    | Exponentiate and assign | `x **= 3`      | `x = x ** 3`       |

---

## Combining Operators in Expressions

You can combine multiple operators in a single expression. Python follows operator precedence rules (e.g., multiplication before addition).

- Use parentheses `()` to group expressions and control evaluation order.

---

## Summary

- Use **arithmetic operators** for mathematical calculations.
- Use **comparison operators** to compare values and get Boolean results.
- Use **logical operators** to combine Boolean expressions.
- Use **assignment operators** to update variable values concisely.
- Combine operators in expressions carefully, respecting operator precedence and using parentheses to clarify.

---

Practice writing expressions combining these operators to strengthen your understanding of Python basics!