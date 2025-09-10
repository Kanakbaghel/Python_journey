## FOR LOOP

### Iterating over a range of numbers

for i in range(5):  # i takes values 0 to 4
    print(i)

### Looping through items in a list
fruits = ['apple','banana','cherry','mango']
for fruit in fruits:
    print(fruit)

## WHILE LOOP

### Example: Counting with while loop
count = 0
while count<5:
    print(count)
    count += 5

## WHILE LOOP

### Repeat until a condition changes
count = 0
while count < 5:
    print(count)
    count += 5

### Excercise

##all even numbers between 2 and 40
even = 0
for i in range(20) :
    print(even)
    even += 2

## Iterate over a list of names and print each name in uppercase.
names = ['Kanak','Kanishka','Kiran','kashish']
for name in names:
    print(name.upper())

## loop to sum numbers from 1 to 100.
count = 1
total = 0
while count <= 100:
    total += count
    count += 1
    
print(f'sum from 1 to 100: {total}')

## loop that asks for user input until the user types "exit".
while True:
    input_user = input(" Write the opposite of entry: ")
    if input_user.lower() == 'exit':
        break
