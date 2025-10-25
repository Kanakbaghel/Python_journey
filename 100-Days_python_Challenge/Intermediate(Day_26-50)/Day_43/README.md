# 100 Days of Python - Day 43: Introduction to Object-Oriented Programming (OOP)

## Overview
Welcome to Day 43 of your 100 Days of Python journey! Today, we introduce **Object-Oriented Programming (OOP)**, a way to organize code by modeling real-world things as "objects." OOP helps make your code reusable, modular, and easier to maintain. We'll focus on three core concepts: **classes**, **objects**, and **encapsulation**.

This project uses simple examples to show how to define classes, create objects, and protect data with encapsulation.

## Learning Objectives
By the end of this day, you should understand:
- What classes and objects are, and how they relate.
- How to define and use classes in Python.
- Encapsulation: Hiding internal details to protect data.
- Basic OOP principles like methods and attributes.
- Why OOP is useful for building larger programs.

## Prerequisites
- Basic knowledge of Python (functions, variables, loops).
- Python 3.x installed.
- No external libraries needed.

## How to Run the Project
1. **Download or Copy Files**: Save the `day43_oop.py` file in a folder.
2. **Open a Terminal/Command Prompt**: Navigate to the folder.
3. **Run the Script**: Type `python day43_oop.py` and press Enter.
4. **View Output**: The script will create objects, call methods, and show results. Experiment by modifying the code!

## Key Concepts Explained Simply
- **Classes**: Like blueprints or templates. They define what an object can do and what data it holds. Example: A `Car` class might have attributes like color and methods like drive.
- **Objects**: Real instances created from a class. Each object has its own data. Example: `my_car = Car("red")` creates a red car object.
- **Encapsulation**: Protecting an object's internal data. In Python, use double underscores (`__`) to make attributes/methods "private" (not easily accessed from outside). This prevents accidental changes.
- **Other Basics**:
  - **Attributes**: Variables inside a class (e.g., `self.name`).
  - **Methods**: Functions inside a class (e.g., `def greet(self):`).
  - **self**: Refers to the current object—always the first parameter in methods.

## Examples from the Code
The `day43_oop.py` script uses a `BankAccount` class for examples:
1. **Defining a Class**: Shows how to create a class with attributes and methods.
2. **Creating Objects**: Instantiates (creates) account objects with different balances.
3. **Using Methods**: Calls methods to deposit, withdraw, and check balance.
4. **Encapsulation**: Demonstrates private attributes (e.g., `__balance`) that can't be accessed directly.
5. **Error Handling**: Shows how encapsulation prevents invalid operations.

Run the script to see objects in action!

## Tips for Learning
- OOP takes practice—start with simple classes and build up.
- Use `self` correctly; it's how objects refer to themselves.
- Encapsulation isn't about secrecy but about safety—use it to control access.
- Read more in Python's official docs or books like "Python Crash Course."
- Avoid overcomplicating; OOP shines in bigger projects.

## Next Steps
- Day 44 could explore inheritance (extending classes) or polymorphism.
- Apply OOP to real projects, like a game or app.
- Share your OOP code for feedback!

Happy coding! OOP might feel abstract at first, but it's powerful once you get it.