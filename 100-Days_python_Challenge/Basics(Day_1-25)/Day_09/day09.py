# Tuple
coordinates = (23,45,23,45)
person = ('Abhijeet', 34, 'Engineer')

#append
t = (1, [2, 3])
t[1].append(4)  # Allowed, because the list inside tuple is mutable
print(t)  # Output: (1, [2, 3, 4])

# Tuple packing 

packed_tuple = 1, "hello", 3.14
print(packed_tuple)  # Output: (1, 'hello', 3.14)

# Tuple unpacking
a, b, c = packed_tuple
print(a)  # 1
print(b)  # hello
print(c)  # 3.14

# Advanced unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
### and
x, _, y = (10, 20, 30)
print(x, y)  # 10 30


## Practice Exercises

"""
1. Create and access tuples
   - Define a tuple with mixed data types.
"""
mixed_tuple = ('Hello', 21, True, 23.34)

"""
   - Access elements by index and slice a sub-tuple.
"""
print(mixed_tuple[1]) #21
print(mixed_tuple[1:3]) #21, True

"""
2. **Tuple packing and unpacking**
   - Pack multiple values into a tuple without parentheses.
"""
pack_tuple = "Apple", 345, "Mango", 234, 23.4

"""
   - Unpack the tuple into variables, including using `*` for variable-length unpacking.
"""
a, *b, c = pack_tuple
print(a) #Apple
print(b) # [345, 'Mango', 234]
print(c) #23.4

"""
3. **Swap variables using tuple unpacking**
"""
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5

"""
4. **Use tuples as dictionary keys**
   - Create a dictionary with tuple keys representing coordinates.
"""
points = {
    (0,0): 'Origin',
    (1,2): 'Point A',
    (3,4): 'Point B'
}

print(points[(1,2)])