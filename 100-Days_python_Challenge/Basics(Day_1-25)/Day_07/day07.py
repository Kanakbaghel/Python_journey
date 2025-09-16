def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Aruhi")  # "Alice" is an argument

## Return Statement
def add(a,b):
    return a+b

result = add(34,56)
result

## Practice
#  two numbers and returns their product.
def mul(a,b):
    return a*b

result = mul(2,5)
result

# checks if a string is a palindrome.
def is_palindrome(s):
    s = s.replace(" ", "" ).lower()
    return s == s[::-1]

print(is_palindrome("Kanak")) #True
print(is_palindrome("Hello")) #False

# converts temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Parameters:
    celsius (float): Temperature in degrees Celsius.
    Returns:
    float: Temperature in degrees Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


