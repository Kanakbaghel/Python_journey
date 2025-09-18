# Local Scope
def greet():
    message = "Hello, World!"  # local variable
    print(message)

greet()
# print(message)  # NameError: name 'message' is not defined

# Global Scope
name = "Alice"  # global variable

def say_name():
    print(name)  # accesses global variable

say_name()  # Output: Alice

# Modifying Global Variables
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Output: 1

#Enclosing (Nonlocal) Scope

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()
    inner()

outer()
# Output:
# 1
# 2
