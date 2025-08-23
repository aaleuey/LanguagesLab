# 1. What is a `lambda` Function?
# -----------------------------------------------------------------------------------------------
'''
unlike a regular function defined with `def` Function,
a `lambda` Function doesn't have a name.
'''
add = lambda a, b: a + b
print(add(3, 4))   # 7

# Equivalent Regular Function Definition
def add(a, b):
    return a + b



# 2. `lambda` Basic Grammar
# -----------------------------------------------------------------------------------------------
lambda parameters: expression

# Example
square = lambda x: x * x
print(square(5))   # 25

greet = lambda name: f"Hi, {name}!"
print(greet("Hana"))   # Hi, Hana!



# 3. When do you Use `lambda`?
# -----------------------------------------------------------------------------------------------
'''
When you need a Simple Function
When you want to pass a short function to functions like `map()`, `filter()`, or `sorted()`
'''



# 4. `map()` Function
# -----------------------------------------------------------------------------------------------
'''
Used when you want to apply the same operation to all elements.
`map(func, iterable)` applies func to every element in iterable.
'''
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)   # [1, 4, 9, 16]

# Equivalent `for` loop
squares = []
for x in nums:
    squares.append(x * x)



# 5. `filter()` Function
# -----------------------------------------------------------------------------------------------
'''
Used when you want to extract only the elements that meet a condition.
`filter(func, iterable)` keeps only the values for which func(x) returns True.
'''
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]



# 6. `lambda` with `sorted()`
# -----------------------------------------------------------------------------------------------
people = [("Hana", 21), ("Hoyoung", 25), ("Maro", 1)]
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)   # [('Maro', 1), ('Hana', 21), ('Hoyoung', 25)]



# 7. `lambda` with `if-else`
# -----------------------------------------------------------------------------------------------
check_even = lambda x: "even" if x % 2 == 0 else "odd"
print(check_even(3))   # odd



# 8. `map` vs `filter` Comparison
# -----------------------------------------------------------------------------------------------
'''
| Function   | Example Usage  | Description                               |
|------------|----------------|-------------------------------------------|
| `map()`    | x * 2          | Applies an operation to all elements      |
| `filter()` | x > 10         | Keeps only elements that meet a condition |
'''



# 9. Practical Example
# -----------------------------------------------------------------------------------------------
# Number list -> string conversion
nums = [1, 2, 3]
str_nums = list(map(lambda x: str(x), nums))
print(str_nums)    # ['1', '2', '3']

# Extract only strings with length 5 or more from a list
words = ["hi", "hello", "python", "bye"]
long_words = list(filter(lambda x: len(x) >= 5, words))
print(long_words)   # ['hello', 'python']



# 10. Nested Usage is also Possible
# -----------------------------------------------------------------------------------------------
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
print(result)   # [4, 8]



# 11. Regular Function vs `lambda` Style Comparison
# -----------------------------------------------------------------------------------------------
# Regular Function
def double(x):
    return x * 2

# `lambda`
double = lambda x: x * 2

'''
Use `def` for readability,
and `lambda` for short, temporary functions.
'''
