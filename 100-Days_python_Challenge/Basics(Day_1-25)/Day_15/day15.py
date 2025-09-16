# Opening a file
file = open("filename.txt", mode)

# Reading from a file

## Read entire content:
content = file.read()

## Read line by line:
line = file.readline()


## Read all lines into a list:
lines = file.readlines()

### 3. Writing to a File

## Write a string:
file.write("Hello, World!\n")

## Write multiple lines:
lines = ["Line 1\n", "Line 2\n"]
file.writelines(lines)

# Cloing a file
### Always close files to free system resources:
file.close()

## Using with statement:
with open("filename.txt", "r") as file:
    content = file.read()

## Example: Reading and Writing Files

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, File Handling!\n")
    file.write("This is a second line.\n")

# Reading from a file
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

