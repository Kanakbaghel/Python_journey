## Use input Function
name = input("Enter your Name: ")

## To get other data types
age = int(input("Enter your age: "))
height = float(input("Enter your Height in meters: "))

## print multiple items
print("Name:", name, "Age:", age)

## customize the separator
print("Hello", "World", sep="-")  # Output: Hello-World
print("Hello", end="!")            # Output: Hello!

#String Formatting with f-strings
name = "Kalpana"
age = 30
print(f'My name is {name} and I am {age} years old.')

#with Numbers
pi = 3.14159
print(f'pi rounded to 2 decimal places: {pi:.2f}')

## Aligning and padding strings
text = "Hi"
print(f'{text:>10}') #Right-align in 10 spaces
print(f'{text:<10}') #Left-align in 10 spaces
print(f'{text:^10}') #Center align in 10 spaces

### Lets take few example for today
# for Simple Input and Output
name = input("What is your name?")
print(f'Hello! {name}')

# Input numbers and formatted output
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
sum = num1 + num2
print(f'The sum of {num1} and {num2} is {sum}.')

#Formatting output with alignment
items = [("Apple",23),("Mango",45),("Banana",34)]
print(f'{'items':<30}{'Quantity':>30}')
for item, qty in items:
    print(f'{item:<30}{qty:<30}')
