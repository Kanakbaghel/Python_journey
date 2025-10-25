# Day 43: Introduction to Object-Oriented Programming (OOP)
# This script demonstrates classes, objects, and encapsulation in Python.
# We'll use a simple BankAccount class as an example.

# Example 1: Defining a Class
# A class is a blueprint. It defines attributes (data) and methods (functions).
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # __init__ is the constructor: runs when an object is created.
        self.owner = owner  # Public attribute: accessible from outside
        self.__balance = initial_balance  # Private attribute: starts with __ (encapsulation)
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    # Method to check balance (read-only access to private attribute)
    def get_balance(self):
        return self.__balance  # Returns the private balance
    
    # Method to show account info
    def account_info(self):
        print(f"Account Owner: {self.owner}, Balance: ${self.__balance}")

# Example 2: Creating Objects (Instances)
# Objects are created from the class. Each has its own data.
account1 = BankAccount("Alice", 100)  # Alice starts with $100
account2 = BankAccount("Bob")         # Bob starts with $0 (default)

print("Example 2 - Creating Objects:")
account1.account_info()  # Shows Alice's info
account2.account_info()  # Shows Bob's info

# Example 3: Using Methods on Objects
# Call methods to interact with the objects.
print("\nExample 3 - Using Methods:")
account1.deposit(50)    # Alice deposits $50
account1.withdraw(30)   # Alice withdraws $30
account2.deposit(200)   # Bob deposits $200

# Example 4: Encapsulation in Action
# Private attributes (__balance) can't be accessed directly from outside.
print("\nExample 4 - Encapsulation:")
print("Alice's balance via method:", account1.get_balance())  # Safe way
# print(account1.__balance)  # This would cause an error (AttributeError) - it's private!
# Instead, try to "hack" it (not recommended):
# account1.__balance = -1000  # This creates a new public attribute, not changing the private one!
print("After 'hack' attempt, balance is still:", account1.get_balance())  # Unchanged!

# Example 5: Demonstrating Protection
# Encapsulation prevents invalid changes.
print("\nExample 5 - Protection with Encapsulation:")
account1.withdraw(200)  # Should fail: insufficient funds
account1.deposit(-10)   # Should fail: negative deposit

# Final state
print("\nFinal Account Info:")
account1.account_info()
account2.account_info()

# Experiment: Create your own class (e.g., a Car with drive() method) and test it!
