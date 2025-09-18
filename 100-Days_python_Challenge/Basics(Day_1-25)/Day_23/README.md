# Day 23: Understanding Python Namespaces and Scopes

Welcome to Day 23! Today, we explore one of the fundamental concepts in Python programming: **namespaces** and **variable scopes**. Understanding how Python manages variable names and their visibility is crucial for writing clear, bug-free code.

---

## What is a Namespace?

- A **namespace** is a container that holds a mapping between **names (identifiers)** and **objects**.
- Think of it as a dictionary where variable names are keys and their corresponding objects are values.
- Different namespaces exist at different levels: built-in, global, and local.

### Types of Namespaces

| Namespace Type | Description                          | Lifetime                      |
|----------------|----------------------------------|-------------------------------|
| Built-in       | Names of built-in functions and exceptions (e.g., `print`, `len`) | Exists as long as Python runs |
| Global         | Names defined at the top-level of a module or script | Exists during the module’s lifetime |
| Local          | Names defined inside a function or block | Exists only during function execution |

---

## Variable Scopes

**Scope** refers to the region of a program where a namespace is directly accessible.

Python follows the **LEGB rule** to resolve variable names:

| Letter | Scope Type       | Description                          |
|--------|------------------|------------------------------------|
| L      | Local            | Names defined inside the current function |
| E      | Enclosing        | Names in the local scopes of any enclosing functions (nested functions) |
| G      | Global           | Names defined at the top-level of the module |
| B      | Built-in         | Names preassigned in the built-in namespace |

---

## Local Scope

Variables defined inside a function are **local** to that function.

---

## Global Scope

Variables defined at the top-level of a module or script are **global**.


### Modifying Global Variables

To modify a global variable inside a function, use the `global` keyword:
Without `global`, assignment inside a function creates a new local variable.

---

## Enclosing (Nonlocal) Scope

In nested functions, the **enclosing** scope refers to the local scope of the outer function.

To modify a variable in the enclosing scope, use the `nonlocal` keyword:

Without `nonlocal`, `count` inside `inner()` would be treated as a new local variable.

---

## Summary

- **Namespaces** map names to objects; Python maintains multiple namespaces simultaneously.
- **Scopes** define where a name can be accessed.
- Python resolves names using the **LEGB** rule: Local → Enclosing → Global → Built-in.
- Use `global` to modify global variables inside functions.
- Use `nonlocal` to modify variables in enclosing (outer) functions.
- Understanding namespaces and scopes helps avoid common bugs related to variable shadowing and unexpected behavior.

---

## Further Reading

- [Python’s official documentation on namespaces and scopes](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Real Python: Understanding Python’s LEGB Rule](https://realpython.com/python-scope-legb-rule/)
- [Python `global` and `nonlocal` keywords](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)

---

Happy coding with clarity and control over your variables! 🧠🐍
