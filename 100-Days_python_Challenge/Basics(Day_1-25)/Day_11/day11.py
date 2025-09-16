# sets
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'apple', 'cherry'}

## Creating Sets
# Using curly braces:
my_set = {1, 2, 3}

# Using the `set()` constructor (useful for creating empty sets or from iterables):
empty_set = set()
from_list = set([1, 2, 2, 3])  # duplicates removed

# Union
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)           # Output: {1, 2, 3, 4, 5}
print(A.union(B))      # Output: {1, 2, 3, 4, 5}

# Intersection
print(A & B)           # Output: {3}
print(A.intersection(B))  # Output: {3}

# Difference
print(A - B)           # Output: {1, 2}
print(A.difference(B)) # Output: {1, 2}

# Symmetric Difference
print(A ^ B)           # Output: {1, 2, 4, 5}
print(A.symmetric_difference(B))  # Output: {1, 2, 4, 5}

# Modifying Sets
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.remove(2)
s.discard(10)  # no error even though 10 not in set
print(s)       # Output: {1, 3, 4, 5, 6}

## Practice Exercises

# 1. Create two sets with some overlapping elements.
X = {2,4,6,8,10}
Y = {1,2,3,4,5}

# 2. Perform union, intersection, difference, and symmetric difference operations.
print(X|Y) #union
print(X.union(Y)) #union

print(X & Y) #intersection
print(X.intersection(Y)) #intersection

print(X - Y) #difference
print(X.difference(Y)) #difference

print(X ^ Y) #symmetric difference
print(X.symmetric_difference(Y)) #symmetric difference

# 3. Add and remove elements from a set.
X.add(3) #add
X.remove(3) #remove

# 4. Check if one set is a subset or superset of another.
X.issubset(Y)      # True if all elements of A are in B
X.issuperset(Y)    # True if A contains all elements of B
X == Y             # True if both sets have the same elements

# 5. Use a set to remove duplicates from a list.
original_list = [1,2,2,3,4,4,4,5,6,3,5]

seen = set()
unique_ordered_list = []

for item in original_list:
    if item not in seen:
        unique_ordered_list.append(item)
        seen.add(item)

print(unique_ordered_list)