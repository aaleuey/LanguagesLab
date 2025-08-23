# 1. Function Definition and Call
# -----------------------------------------------------------------------------------------------
def greet():
    print("Hello!")

greet()   # Call the function



# 2. Parameter and Argument
# -----------------------------------------------------------------------------------------------
def greet(name):
    print(f"Hello, {name}!")

greet("Hana")



# 3. Default Argument
# -----------------------------------------------------------------------------------------------
def greet(name="hamster"):
    print(f"Hello, {name}!")

greet()         # Hello, hamster!
greet("Maro")   # Hello, Maro!



# 4. Return Value
# -----------------------------------------------------------------------------------------------
def square(x):
    return x ** 2

result = square(5)
print(result)   # 25



# 5. Multiple Return Values
# -----------------------------------------------------------------------------------------------
def calc(a, b):
    return a + b, a * b   # returns multiple values: sum and product

add, mul = calc(3, 4)
print(add, mul)   # 7 12 



# 6. Keyword Arguments & Positional Arguments
# -----------------------------------------------------------------------------------------------
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Hana", 21)               # positional arguments
introduce(age=25, name="Hoyoung")   # keyword arguments (order doesn't matter)



# 7. Variable Arguments (`*args`, `**kwargs`)
# -----------------------------------------------------------------------------------------------
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))   # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Hana", age=21)



# 8. Nested Function
# -----------------------------------------------------------------------------------------------
def outer():
    def inner():
        print("Inner function")
    inner()

outer()



# 9. Functions are Objects (Assigning to a variable, Passing as an argument)
# -----------------------------------------------------------------------------------------------
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    print(func("Hello"))

greet(shout)     # HELLO
greet(whisper)   # hello



# 10. Docstring
# -----------------------------------------------------------------------------------------------
def add(x, y):
    """
    Adds two numbers.
    
    Parameters:
        x (int): The first number
        y (int): The second number
    
    Returns:
        int: The sum of x and y
    """
    return x + y

print(add.__doc__)



# 11. Recursive Function (a function that calls itself)
# -----------------------------------------------------------------------------------------------
def factorial(n):
    '''
    Calculate the factorial of n recursively.
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))   # 120
