age  = 20

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else :
    print("Adult")

## checks if a number is positive, negative, or zero
num = input("Enter any integer number: ")

if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Try Again with Integer Number")

## assigns letter grades based on score ranges
score = 54

if score < 20:
    print("Grade D")
elif score < 40:
    print("Grade C")
elif score < 60:
    print("Grade B")
elif score < 80:
    print("Grade B+")
else:
    print("Grade A")

## login check that verifies username and password.
correct_username = "Kanak_345"
correct_password = 123456789

username = input("Enter your username: ")
password = input ("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid! Try Again... ")
