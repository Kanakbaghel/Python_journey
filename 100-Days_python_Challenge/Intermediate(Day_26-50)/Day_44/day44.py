# Day 44: Classes, Objects, Methods, and Attributes
# This script demonstrates writing your own classes, instantiating objects, and using methods/attributes.
# We'll define two example classes: Book and Student.

# Example 1: Defining a Book Class
# A class for representing books with attributes like title and author, and a method to "read" it.
class Book:
    def __init__(self, title, author):
        # Constructor: Sets up the object with initial attributes.
        self.title = title      # Instance attribute: unique to each book
        self.author = author    # Instance attribute
        self.is_read = False    # Instance attribute: tracks if the book has been read
    
    def read(self):
        # Method: Simulates reading the book and marks it as read.
        if not self.is_read:
            print(f"Reading '{self.title}' by {self.author}...")
            self.is_read = True
        else:
            print(f"You've already read '{self.title}'.")
    
    def info(self):
        # Method: Prints book details.
        status = "read" if self.is_read else "unread"
        print(f"Book: '{self.title}' by {self.author} - Status: {status}")

# Example 2: Instantiating Book Objects
# Create objects (instances) from the Book class.
book1 = Book("1984", "George Orwell")  # Instantiates a Book object
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print("Example 2 - Creating Book Objects:")
book1.info()  # Calls the info method on book1
book2.info()  # Calls the info method on book2

# Example 3: Using Methods and Attributes on Book Objects
# Interact with the objects by calling methods and accessing attributes.
print("\nExample 3 - Using Book Methods and Attributes:")
book1.read()  # Calls read() method
print(f"book1.title: {book1.title}")  # Accesses attribute directly
book1.read()  # Tries to read again (should show already read)
book2.read()  # Reads book2

# Example 4: Defining a Student Class with More Features
# A class for students, including instance attributes, methods, and a class attribute.
class Student:
    school = "Python Academy"  # Class attribute: shared by all Student objects
    
    def __init__(self, name):
        self.name = name              # Instance attribute
        self.grades = []              # Instance attribute: list of grades
    
    def add_grade(self, grade):
        # Method: Adds a grade to the student's list.
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} for {self.name}.")
        else:
            print("Grade must be between 0 and 100.")
    
    def average_grade(self):
        # Method: Calculates and returns the average grade.
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0
    
    def info(self):
        # Method: Prints student details.
        avg = self.average_grade()
        print(f"Student: {self.name} at {self.school}")
        print(f"Grades: {self.grades}, Average: {avg:.2f}")

# Example 5: Instantiating Student Objects and Using Them
# Create student objects and demonstrate methods/attributes.
student1 = Student("Alice")  # Instantiates a Student object
student2 = Student("Bob")

print("\nExample 5 - Creating and Using Student Objects:")
student1.add_grade(85)  # Calls method
student1.add_grade(92)
student1.info()         # Calls info method

student2.add_grade(78)
student2.add_grade(88)
student2.info()

# Accessing class attribute (shared)
print(f"\nAll students attend: {Student.school}")  # Via class
print(f"Alice's school: {student1.school}")       # Via object (same thing)

# Experiment: Create your own class (e.g., a Car with drive() method) and instantiate objects!
# Try adding more attributes or methods to the existing classes.
