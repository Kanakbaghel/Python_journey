### Example Usage of Math
import math

# Constants
print(math.pi)  # 3.141592653589793

# Square root
print(math.sqrt(16))  # 4.0

# Logarithm base e
print(math.log(math.e))  # 1.0

# Trigonometry
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(math.sin(angle_rad))  # 0.7071067811865475

# Factorial
print(math.factorial(5))  # 120

### Example Usage of Dates

from datetime import date, datetime, timedelta

# Current date and time
now = datetime.now()
print(now)  # e.g., 2024-06-15 14:30:00.123456

# Create a specific date
birthday = date(1990, 12, 25)
print(birthday)  # 1990-12-25

# Date arithmetic
tomorrow = birthday + timedelta(days=1)
print(tomorrow)  # 1990-12-26

# Difference between dates
days_until_birthday = (birthday - date.today()).days
print(f"Days until birthday: {days_until_birthday}")

# Formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # e.g., "2024-06-15 14:30:00"
