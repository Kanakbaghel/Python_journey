### Example Usage with json
import json

# Reading JSON from a file
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)

# Writing JSON to a file
new_data = {'name': 'Alice', 'age': 30, 'is_member': True}
with open('output.json', 'w') as f:
    json.dump(new_data, f, indent=4)

# Converting Python object to JSON string
json_str = json.dumps(new_data)
print(json_str)

# Parsing JSON string back to Python object
parsed = json.loads(json_str)
print(parsed)

### Example Usage with csv

import csv

# Reading CSV file
with open('data.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Writing CSV file
rows = [
    ['Name', 'Age', 'City'],
    ['Bob', '25', 'New York'],
    ['Jane', '29', 'San Francisco']
]
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Using DictReader and DictWriter
with open('data.csv', 'r', newline='') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(row['Name'], row['Age'])

with open('output_dict.csv', 'w', newline='') as f:
    fieldnames = ['Name', 'Age', 'City']
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader()
    dict_writer.writerow({'Name': 'Alice', 'Age': 30, 'City': 'Boston'})
