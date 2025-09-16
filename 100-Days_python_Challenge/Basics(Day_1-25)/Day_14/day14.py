### 1. Catching Specific Exceptions
try:
    result = 10 / divisor
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

### 2. Catching Multiple Exceptions
try:
    value = int(user_input)
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Input error: {e}")

### 3. Catching All Exceptions (Use with Caution)
try:
    do_something()
except Exception as e:
    print(f"Unexpected error: {e}")

### 4. The `else` Clause
try:
    data = fetch_data()
except IOError:
    print("Failed to read data.")
else:
    process(data)

### 5. The `finally` Clause
try:
    file = open("data.txt")
    data = file.read()
except IOError:
    print("File error.")
finally:
    file.close()


## Example: Robust User Input
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        print(f"Your age is {age}.")
        break