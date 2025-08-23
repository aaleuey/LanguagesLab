# 1. Basic Variable Declaration
# -----------------------------------------------------------------------------------------------
name = "Hana"
age = 21
height = 159.7
is_student = True

print(name, age, height, is_student)   # Daa 21 159.7 True



# 2. Checking Data Types and Type Hint
# -----------------------------------------------------------------------------------------------
print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(height))       # <class 'float'>
print(type(is_student))   # <class 'bool'>

# Type Hint (Python 3.5+)
def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old."



# 3. Dynamic Typing in Variables
# -----------------------------------------------------------------------------------------------
x = 10
print(type(x))   # int

x = "hello"
print(type(x))   # str

'''
In Python, variables are dynamically typed,
so the same variable x can first store an integer and later store a string.
The type() function helps you check what type of data a variable currently holds.
'''


# 4. Type Conversion
# -----------------------------------------------------------------------------------------------
a = "100"
b = int(a)   # str -> int

c = 3.14
d = str(c)   # float -> str

print(type(b))   # int
print(type(d))   # str



# 5. `id()` and memory address
# -----------------------------------------------------------------------------------------------
x = 10
y = 10
print(id(x), id(y))   # Same object (small integers are cached)

z = 1000
w = 1000
print(id(z), id(w))   # May be different (large integers are not always cached)

'''
In Python, small integers (typically from -5 to 256) are cached and reused to save memory.
So variables with the same small integer value will usually point to the same object in memory.

Larger integers, like 1000, are not guaranteed to be cached.
So even if they have the same value, they may refer to different objects in memory.
'''



# 6. Immutable types vs Mutable types
# -----------------------------------------------------------------------------------------------
# Immutable types: int, float, str, tuple
a = "hi"
print(id(a))
a += " there"
print(id(a))    # A new object is created (different ID)

# Mutable types: list, dict, set
lst = [1, 2]
print(id(lst))
lst.append(3)
print(id(lst))   # The same object is modified (ID stays the same)



# 7. Declaring Multiple Variables and Unpacking
# -----------------------------------------------------------------------------------------------
# Assign multiple variables simultaneously
x, y, z = 1, 2, 3

# Unpacking
a, b = [10, 20]

# Swap variables this way too
x, y = y, x
print(x, y)  # 2 1



# 8. Constant-like variable (Uppercase Naming Convention)
# -----------------------------------------------------------------------------------------------
PI = 3.14159
GRAVITY = 9.8

'''
In Python, there is no built-in way to create true constants,
but by convention, variabels with names in all uppercase letters are treated as constants - values that should not be changed.
'''



# 9. None and Null
# -----------------------------------------------------------------------------------------------
x = None
print(x is None)  # True

'''
In Python, None is a special built-in constant that represents the absence of a value.
'''
