# Dictionary
Person = {
    "name" : "Kanak Baghel",
    "age" : 21,
    "state" : "Haryana"
}

# Accessing Values
print(Person["name"])
print(Person.get("country"))   # Output: None
print(Person.get("country", "India"))  # Output: India

# Adding and Updating items
Person["Email"] = "kanakbaghel@example.com" #add
Person["age"] = 32 #update

# Deleting Items
del Person["state"]
email = Person.pop("email")
last_item = Person.popitem()
Person.clear()

## Example: Complete Dictionary Usage

# Create dictionary
student = {
    "name": "John",
    "age": 22,
    "courses": ["Math", "Physics"]
}

# Access values
print(student["name"])  # John

# Add new item
student["grade"] = "A"

# Update item
student["age"] = 23

# Delete item
del student["courses"]

# Safe access
print(student.get("courses", "No courses found"))

# Iterate over keys and values
for key, value in student.items():
    print(f"{key}: {value}")

## Practice Exercises

# 1. Create a dictionary representing a book with keys: title, author, year, and pages.
sample_book = {
    "title" : "A Sample Story of Life",
    "author" : "W.C Sphere",
    "year" : "2002",
    "pages" : "465"
}

# 2. Add a new key `publisher` to the dictionary.
sample_book["publisher"] = "John richer"
sample_book

#3. Update the year of publication.
sample_book["year"] = 1987

#4. Delete the pages key.
del sample_book["pages"]

#5. Use `.get()` to safely access a key that may not exist.
# Access 'isbn' key which may not exist, provide default value None
isbn = sample_book.get("isbn")
print(isbn)  # Output: None

# Access 'publisher' key with a default fallback
publisher = sample_book.get("publisher", "Unknown Publisher")
print(publisher)  

#6. Iterate over the dictionary and print all key-value pairs.
for key, value in sample_book.items():
    print(f"{key}:{value}")