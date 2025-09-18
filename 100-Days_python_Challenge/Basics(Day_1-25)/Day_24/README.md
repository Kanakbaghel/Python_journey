# Day 24: Recursion Basics

Welcome to Day 24! Today, we explore **recursion**, a powerful programming technique where a function calls itself to solve smaller instances of a problem. Understanding recursion will help you tackle problems that have a naturally recursive structure, such as tree traversals, factorial calculations, and more.

---

## What is Recursion?

- **Recursion** is a method where a function solves a problem by calling itself with a simpler or smaller input.
- Each recursive call breaks the problem down until it reaches a **base case**, which stops the recursion.
- Without a base case, recursion leads to infinite calls and eventually a stack overflow.

---

## Anatomy of a Recursive Function

A recursive function typically has two parts:

1. **Base Case**: The condition under which the function returns a value without making further recursive calls.
2. **Recursive Case**: The part where the function calls itself with a smaller or simpler argument.

---

## Example 1: Factorial Function

The factorial of a non-negative integer \$n\$ is defined as:

\$$
n! = \begin{cases}
1 & \text{if } n = 0 \\
n \times (n-1)! & \text{if } n > 0
\end{cases}
\$$

---

## Example 2: Fibonacci Sequence

The Fibonacci sequence is defined as:

\$$
F_n = \begin{cases}
0 & \text{if } n = 0 \\
1 & \text{if } n = 1 \\
F_{n-1} + F_{n-2} & \text{if } n > 1
\end{cases}
\$$

---

## Important Points

- **Always define a base case** to prevent infinite recursion.
- Recursive calls add to the **call stack**; deep recursion can lead to a stack overflow.
- Some problems are more efficiently solved with **iteration** or **memoization** to avoid redundant calculations.
- Recursion is elegant and intuitive for problems with self-similar structure.

---

## Visualizing Recursion

For `factorial(3)`, the calls unfold as:

```
factorial(3)
= 3 * factorial(2)
= 3 * (2 * factorial(1))
= 3 * (2 * (1 * factorial(0)))
= 3 * (2 * (1 * 1))
= 6
```

---

## Summary

- Recursion is a function calling itself to solve smaller subproblems.
- Must have a **base case** to terminate recursion.
- Useful for problems like factorial, Fibonacci, tree traversals, and divide-and-conquer algorithms.
- Understand recursion depth and performance implications.

---

## Further Reading

- [Python official tutorial on recursion](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Visualizing recursion with Python Tutor](https://pythontutor.com/)
- [Real Python: Understanding Recursion in Python](https://realpython.com/python-recursion/)

---

Happy recursive thinking! 🔄🐍
