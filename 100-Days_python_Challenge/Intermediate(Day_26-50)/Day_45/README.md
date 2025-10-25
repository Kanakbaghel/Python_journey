# 100 Days of Python - Day 45: Inheritance and Polymorphism Basics

## Overview
Welcome to Day 45 of your 100 Days of Python journey! Today, we explore **inheritance** and **polymorphism**, two key OOP concepts. **Inheritance** lets one class "inherit" features from another, like a child inheriting traits from parents. **Polymorphism** allows the same method to behave differently in subclasses, making code flexible.

This project demonstrates extending classes (inheritance) and overriding methods (polymorphism) with a simple `Animal` example.

## Learning Objectives
By the end of this day, you should understand:
- How inheritance works: Creating subclasses that build on a base class.
- Overriding methods: Redefining inherited methods in subclasses.
- Polymorphism: Using the same method name for different behaviors.
- When to use these concepts for cleaner, reusable code.

## Prerequisites
- Completion of Days 43-44 (basic OOP with classes/objects).
- Basic Python skills.
- Python 3.x installed.
- No external libraries needed.

## How to Run the Project
1. **Download or Copy Files**: Save the `day45_inheritance_polymorphism.py` file in a folder.
2. **Open a Terminal/Command Prompt**: Navigate to the folder.
3. **Run the Script**: Type `python day45_inheritance_polymorphism.py` and press Enter.
4. **View Output**: The script will show inheritance and polymorphism in action. Experiment by modifying subclasses!

## Key Concepts Explained Simply
- **Inheritance**: A subclass (child) inherits attributes and methods from a base class (parent). Use `class SubClass(BaseClass):`. The child can add new features or change existing ones.
- **Overriding Methods**: In a subclass, redefine a method from the parent to change its behavior. The subclass version takes precedence.
- **Polymorphism**: "Many forms"—the same method (e.g., `speak()`) can do different things in different classes. It allows treating objects uniformly (e.g., a list of animals all "speaking").
- **super()**: Calls the parent's method from a subclass, useful for extending (not replacing) behavior.

## Examples from the Code
The `day45_inheritance_polymorphism.py` script uses an `Animal` base class with `Dog` and `Cat` subclasses:
1. **Defining a Base Class**: `Animal` with attributes and a `speak()` method.
2. **Inheritance**: `Dog` and `Cat` inherit from `Animal` and add/override features.
3. **Overriding Methods**: `Dog` and `Cat` override `speak()` for unique sounds.
4. **Polymorphism**: A list of animals calls the same `speak()` method, but each behaves differently.
5. **Using super()**: Shows extending parent methods instead of fully overriding.

Run the script to see animals "speaking"!

## Tips for Learning
- Inheritance reduces code duplication—reuse parent code in children.
- Override only when needed; use `super()` to build on the parent.
- Polymorphism is great for lists or loops where objects share a method but act differently.
- Sketch a hierarchy (e.g., Vehicle -> Car, Truck) before coding.
- Avoid deep inheritance chains—keep it simple.

## Next Steps
- Day 46 could cover more advanced OOP, like abstract classes or multiple inheritance.
- Challenge: Create your own inheritance hierarchy (e.g., Shape -> Circle, Rectangle).
- Apply to projects, like a game with character classes.

Happy coding! Inheritance and polymorphism make OOP powerful—practice by extending the examples.