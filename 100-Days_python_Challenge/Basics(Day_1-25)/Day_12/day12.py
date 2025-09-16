## Key String Methods
# Split
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

#join
fruits = ['apple', 'banana', 'cherry']
text = ", ".join(fruits)
print(text)  # Output: apple, banana, cherry

#replace
text = "Hello world! Hello everyone!"
new_text = text.replace("Hello", "Hi", 1)
print(new_text)  # Output: Hi world! Hello everyone!

#strip
text = "   Hello World!   "
clean_text = text.strip()
print(clean_text)  # Output: Hello World!

# find
text = "Hello world"
index = text.find("world")
print(index)  # Output: 6

## Practice Exercises

#1. Split a comma-separated string into a list of items.
csv_string = "apple,orange,banana,mango,cherry"
items = csv_string.split(",")
print(items)

#2. Join a list of words into a single string separated by hyphens (`-`).
joined_string = "-".join(csv_string)
print(joined_string)

#3. Replace all occurrences of a substring in a string.
text = "I like cats. Cats are great pets."
new_text = text.replace("cats","dogs").replace("Cats","Dogs")
print(new_text)

#4. Strip whitespace and special characters from user input.
user_input = "  \n\t Hello, World! \t\n "
clean_input = user_input.strip()
print(f"'{clean_input}'")  

#5. Find the position of a substring and handle the case when it is not found.
text = "Find the needle in the yard."
substring = "needle"

position = text.find(substring)
if position != -1:
    print(f"Substring '{substring}' found at position {position}.")
else:
    print(f"Substring '{substring}' not found.")