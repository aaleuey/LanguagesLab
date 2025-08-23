# 1. Input and Output related
# -----------------------------------------------------------------------------------------------
print("Hello")   # Display output on the screen
name = input("What's your name? ")   # Get user input



# 2. Numeric Functions
# -----------------------------------------------------------------------------------------------
abs(-7)             # 7 (absolute value)
pow(2, 3)           # 8 (2 to the power of 3)
round(3.14159, 2)   # 3.14 (rounded to 2 decimal places)

max(3, 5, 1)        # 5 (maximum value)
min(3, 5, 1)        # 1 (minimum value)
sum([1, 2, 3])      # 6 (sum of all elements)

divmod(10, 3)       # (3, 1) (Returns the quotient and remainder as a tuple)
int(3.9)            # 3   (Converts float to integer (truncates decimal))
float(5)            # 5.0 (Converts integer to float)



# 3. Type Conversion Functions
# -----------------------------------------------------------------------------------------------
int("10")        # 10 (convert string to integer)
float("3.14")    # 3.14 (convert string to float)
str(100)         # "100" (convert integer to string)
bool(0)          # False (convert integer to boolean)
list("abc")      # ['a', 'b', 'c'] (convert string to list of characters)
tuple([1, 2])    # (1, 2) (convert list to tuple)
set([1, 1, 2])   # {1, 2} (convert list to set, removes duplicates)
dict([[1, 'a'], [2, 'b']])   # {1: 'a', 2: 'b'} (convert list of key-value pairs to dictionary)



# 4. Iteration-related Functions
# -----------------------------------------------------------------------------------------------
range(5)                  # Generates numbers from 0 to 4
enumerate(["a", "b"])     # Returns tuples of (index, value)
zip([1, 2], ['a', 'b'])   # Pairs elements as (1, 'a'), (2, 'b')

for i, v in enumerate(["a", "b"]):
    print(i, v)



# 5. Type checking and Sorting
# -----------------------------------------------------------------------------------------------
type(3.14)           # <class 'float'> (checks the data type of 3.14)
isinstance(5, int)   # True (checks if 5 is an instance of int)

sorted([3, 1, 2])             # [1, 2, 3] (returns a sorted list)
sorted(["banana", "apple"])   # ['apple', 'banana'] (returns a sorted list of strings)



# 6. Higher-order Function (a function that takes another function as an argument)
# -----------------------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * 2, numbers)))          # [2, 4, 6, 8, 10]
print(list(filter(lambda x: x % 2 ==0, numbers)))   # [2, 4] (filters even numbers)

'''
map(): Applies a function to each element
filter(): filters elements that satisfy a condition
'''



# 7. Other useful built-in Functions
# -----------------------------------------------------------------------------------------------
len("hello")         # 5
reversed("abc")      # ['c', 'b', 'a']
all([True, True])    # True  (returns True if all elements are True)
any([False, True])   # True  (returns True if any elements is True)
chr(97)              # 'a'   (returns character for ASCII code 97)
ord('a')             # 97    (returns ASCII code of character 'a')
