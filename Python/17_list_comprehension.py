# 1. Basic Grammar
# -----------------------------------------------------------------------------------------------
# Expressing a typical `for-loop` in one line.
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Typical way
squares = []
for x in range(5):
	squares.append(x * x)



# 2. Including a Conditional Statement
# -----------------------------------------------------------------------------------------------
# You can filter using a conditional statement.
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]



# 3. Including `if-else` (ternary operator style)
# -----------------------------------------------------------------------------------------------
# Use it when you want to assign different values based on a condition.
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)   # ['even', 'odd', 'even', 'odd', 'even']



# 4. Used for string processing
# -----------------------------------------------------------------------------------------------
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 6, 6]

uppercased = [w.upper() for w in words]
print(uppercased)  # ['APPLE', 'BANANA', 'CHERRY']



# 5. Nested Loops
# -----------------------------------------------------------------------------------------------
# Nested Loops can also be expressed in one line.
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)   # [(0, 0), (0, 1), (0, 2), (1, 0), ...]



# 6. Used with collections other than lists
# -----------------------------------------------------------------------------------------------
sentence = "I love Python"
chars = [c for c in sentence if c != " "]
print(chars)



# 7. Creating a 2D List
# -----------------------------------------------------------------------------------------------
matrix = [[x * y for x in range(1, 4)] for y in range(1, 4)]
for row in matrix:
    print(row)   # [1, 2, 3]
                 # [2, 4, 6]
                 # [3, 6, 9]



# 8. Dictionary/Set Comprehension
# -----------------------------------------------------------------------------------------------
# Dictionary
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)    # {0: 0, 1: 1, 2: 4, ...}

# Set
unique_lengths = {len(word) for word in ["hi", "hello", "python", "hi"]}
print(unique_lengths)   # {2, 5, 6}



# 9. Practical Example
# -----------------------------------------------------------------------------------------------
# 1: Create a list of perfect squares(√n) between 1 and 100 (√n is an integer)
squares = [x for x in range(1, 101) if (x ** 0.5).is_integer()]
print(squares)   # [1, 4, 9, 16, ..., 100]

# 2: Extracting only numbers from a list
mixed = ["apple", 11, "banana", 19, None, 20.24]
numbers = [x for x in mixed if isinstance(x, (int, float))]
print(numbers)   # [11, 19, 20.24]

# 3: Convert only words with length 5 or more to uppercase
words = ["hi", "hello", "python", "go"]
filtered = [w.upper() for w in words if len(w) >= 5]
print(filtered)   # ['HELLO', 'PYTHON']
