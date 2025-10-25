# 100 Days of Python - Day 44: Classes, Objects, Methods, and Attributes

## Overview
Welcome to Day 44 of your 100 Days of Python journey! Building on Day 43's introduction to OOP, today we focus on **writing your own classes**, **instantiating objects**, and mastering **methods and attributes**. You'll learn to create custom blueprints (classes) for real-world things, bring them to life as objects, and add behaviors (methods) and data (attributes).

This project provides hands-on examples with two simple classes: `Book` and `Student`. You'll define them, create objects, and interact with them.

## Learning Objectives
By the end of this day, you should understand:
- How to define your own classes with attributes and methods.
- Instantiating (creating) objects from classes.
- Using instance attributes (unique to each object) and class attributes (shared).
- Calling methods on objects to perform actions.
- Best practices for organizing code with OOP.

## Prerequisites
- Completion of Day 43 (basic OOP knowledge).
- Basic Python skills (functions, variables).
- Python 3.x installed.
- No external libraries needed.

## How to Run the Project
1. **Download or Copy Files**: Save the `day44_oop_classes.py` file in a folder.
2. **Open a Terminal/Command Prompt**: Navigate to the folder.
3. **Run the Script**: Type `python day44_oop_classes.py` and press Enter.
4. **View Output**: The script will create objects, call methods, and print results. Modify the code to experiment!

## Key Concepts Explained Simply
- **Defining Classes**: Use the `class` keyword. Inside, define `__init__` (constructor) for setup, and methods for actions.
- **Attributes**: Data stored in objects. Instance attributes (e.g., `self.title`) are unique per object. Class attributes (e.g., `species = "Human"`) are shared.
- **Methods**: Functions inside classes that operate on the object. They always start with `self`.
- **Instantiating Objects**: Create an object like `my_book = Book("Title", "Author")`. Each object is independent.
- **self**: Refers to the current object—use it to access attributes/methods.

## Examples from the Code
The `day44_oop_classes.py` script includes these examples:
1. **Defining and Instantiating a Book Class**: Creates `Book` objects with title/author attributes and a `read` method.
2. **Using Instance Attributes**: Each book has its own title and author.
3. **Defining and Instantiating a Student Class**: Creates `Student` objects with name/grades, and methods to add grades and calculate averages.
4. **Class Attributes**: Shows a shared attribute (e.g., school name).
5. **Calling Methods**: Demonstrates actions like reading a book or updating student grades.

Run the script to see objects interacting!

## Tips for Learning
- Start simple: Pick a real-world thing (e.g., a car or pet) and model it as a class.
- Always use `self` in methods to refer to the object.
- Test your classes by creating multiple objects and calling methods.
- OOP encourages reusability—write classes you can use in future projects.
- If stuck, sketch the class on paper first (attributes as nouns, methods as verbs).

## Next Steps
- Day 45 could introduce inheritance (one class inheriting from another).
- Challenge: Create a class for something fun, like a `GameCharacter`, and share it.
- Practice by refactoring procedural code into OOP.

Happy coding! Writing classes is like building Lego blocks—start small and build up.