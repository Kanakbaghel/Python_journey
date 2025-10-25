# Day 45: Inheritance and Polymorphism Basics
# This script demonstrates inheritance (extending classes) and polymorphism (overriding methods).
# We'll use a base Animal class with Dog and Cat subclasses.

# Example 1: Defining a Base Class (Parent)
# The Animal class is the base. Subclasses will inherit from it.
class Animal:
    def __init__(self, name, species):
        self.name = name        # Instance attribute
        self.species = species  # Instance attribute
    
    def speak(self):
        # Base method: Default sound for any animal.
        return f"{self.name} makes a sound."
    
    def info(self):
        # Method to display animal details.
        print(f"{self.name} is a {self.species}.")

# Example 2: Inheritance - Creating a Subclass (Child)
# Dog inherits from Animal. It gets all Animal features but can add/override.
class Dog(Animal):  # Dog extends Animal
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent's __init__ with super()
        self.breed = breed             # New attribute specific to Dog
    
    def speak(self):
        # Override: Changes the speak method for dogs.
        return f"{self.name} barks: Woof!"
    
    def fetch(self):
        # New method: Only dogs can fetch.
        print(f"{self.name} fetches the ball.")

# Another subclass: Cat
class Cat(Animal):  # Cat extends Animal
    def __init__(self, name, color):
        super().__init__(name, "Cat")  # Call parent's __init__
        self.color = color             # New attribute specific to Cat
    
    def speak(self):
        # Override: Changes the speak method for cats.
        return f"{self.name} meows: Meow!"
    
    def climb(self):
        # New method: Only cats can climb.
        print(f"{self.name} climbs the tree.")

# Example 3: Instantiating Objects from Subclasses
# Create objects: They inherit from Animal but have subclass-specific features.
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Black")

print("Example 3 - Creating Subclass Objects:")
dog1.info()  # Inherited method
cat1.info()  # Inherited method

# Example 4: Overriding Methods
# Call speak() on each: Shows overridden behavior.
print("\nExample 4 - Overriding Methods:")
print(dog1.speak())  # Dog's version: Woof!
print(cat1.speak())  # Cat's version: Meow!

# Example 5: Polymorphism in Action
# Polymorphism: Same method name, different behaviors. Treat a list of animals uniformly.
animals = [dog1, cat1]  # List of different animal types
print("\nExample 5 - Polymorphism:")
for animal in animals:
    print(animal.speak())  # Each calls its own speak() - same method, different output

# Bonus: Using super() to Extend (Not Fully Override)
# Modify Dog to add to the parent's speak instead of replacing it.
class LoudDog(Dog):  # Inherits from Dog
    def speak(self):
        # Use super() to call parent's speak, then add more.
        parent_sound = super().speak()  # Gets "Buddy barks: Woof!"
        return f"{parent_sound} (very loudly!)"

loud_dog = LoudDog("Max", "Bulldog")
print("\nBonus - Extending with super():")
print(loud_dog.speak())  # Combines parent and new behavior

# Experiment: Create your own subclass (e.g., Bird) and override speak()!
# Try adding polymorphism to a loop with more animals.
