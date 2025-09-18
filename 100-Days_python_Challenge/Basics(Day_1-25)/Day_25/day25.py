
## Problem 1: Count Vowels in a String

# Write a function that takes a string and returns the number of vowels (`a, e, i, o, u`) it contains.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
print(count_vowels("Hello World"))  # Output: 3


## Problem 2: Find the Maximum Number in a List

# Write a function that takes a list of numbers and returns the maximum value without using the built-in `max()` function.

def find_max(numbers):
    if not numbers:
        return None  # Handle empty list
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Example
print(find_max([3, 7, 2, 9, 5]))  # Output: 9

## Problem 3: Fibonacci Sequence Generator

# Write a function that returns a list containing the first `n` Fibonacci numbers.
def fibonacci_sequence(n):
    if n <= 0:
        return []
    sequence = [0]
    if n == 1:
        return sequence
    sequence.append(1)
    for _ in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

# Example
print(fibonacci_sequence(7))  # Output: [0, 1, 1, 2, 3, 5, 8]

## Problem 4: Remove Duplicates from a List

# Write a function that removes duplicates from a list while preserving the original order.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example
print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))  # Output: [1, 2, 3, 4, 5]

## Problem 5: Check for Palindrome

# Write a function that checks if a given string is a palindrome (reads the same forwards and backwards), ignoring case and spaces.

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
