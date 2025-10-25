# Day 41: Introduction to Regular Expressions in Python
# This script demonstrates basic regex for pattern matching and text extraction.
# We use Python's built-in 're' module. Regex helps find patterns in text, like emails or numbers.

import re  # Import the regular expressions module

# Example 1: Matching a simple pattern at the start of a string
# re.match() checks if the pattern matches from the beginning.
pattern = r"Hello"  # 'r' makes it a raw string (ignores backslashes)
text = "Hello, world!"
match = re.match(pattern, text)
if match:
    print("Example 1 - Match found:", match.group())  # Prints "Hello"
else:
    print("Example 1 - No match")

# Example 2: Searching for a word anywhere in the text
# re.search() finds the first occurrence of the pattern.
pattern = r"Python"
text = "I love learning Python and coding."
search_result = re.search(pattern, text)
if search_result:
    print("Example 2 - Found:", search_result.group())  # Prints "Python"
else:
    print("Example 2 - Not found")

# Example 3: Extracting emails from text
# re.findall() returns all matches as a list. This pattern matches basic email formats.
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "Contact us at info@example.com or support@site.org for help."
emails = re.findall(pattern, text)
print("Example 3 - Emails found:", emails)  # Prints ['info@example.com', 'support@site.org']

# Example 4: Finding phone numbers in a specific format (e.g., 123-456-7890)
# \d{3} means exactly 3 digits.
pattern = r"\d{3}-\d{3}-\d{4}"
text = "Call me at 123-456-7890 or 987-654-3210."
phones = re.findall(pattern, text)
print("Example 4 - Phone numbers:", phones)  # Prints ['123-456-7890', '987-654-3210']

# Example 5: Replacing text using regex
# re.sub() replaces matches with new text.
pattern = r"bad"
text = "This is a bad example."
new_text = re.sub(pattern, "good", text)
print("Example 5 - Replaced text:", new_text)  # Prints "This is a good example."

# Bonus: A more complex example - Extracting words starting with a capital letter
# \b[A-Z]\w* : Word boundary, capital letter, followed by word characters.
pattern = r"\b[A-Z]\w*"
text = "Python is Great for Beginners."
capitals = re.findall(pattern, text)
print("Bonus - Capital words:", capitals)  # Prints ['Python', 'Great', 'Beginners']

# Experiment: Try changing the 'text' variables above and run the script again!
