# 1. Basic Structrue
# -----------------------------------------------------------------------------------------------
try:
    # Code that may raise an error
    x = 1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")



# 2. Various Exception Handling
# -----------------------------------------------------------------------------------------------
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("You entered a non-numeric value.")
except ZeroDivisionError:
    print("You cannot divide by zero.")



# 3. Catching All Exception (Not recommended, but possible)
# -----------------------------------------------------------------------------------------------
try:
    risky()
except Exception as e:
    print("An exception occurred:", e)



# 4. `else` and `finally`
# -----------------------------------------------------------------------------------------------
try:
    print("Division result:", 10 / 2)
except ZeroDivisionError:
    print("An error occurred!")
else:
    print("Executed successfully")   # Runs only if no exception occurs
finally:
    print("This always runs")        # Runs no matter what

'''
try:      Always executed (code that might raise an exception)
except:   Executed only if an exception occurs in try block
else:     Executed only if try block runs without error
finally:  Always executed, regardless of whether an exception occurred
'''



# 5. raise statement (manually raising an exception)
# -----------------------------------------------------------------------------------------------
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

print(divide(10, 0))  # Raises ValueError



# 6. User-defined Exception
# -----------------------------------------------------------------------------------------------
class MyError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise MyError("Age must be 0 or greater.")

try:
    check_age(-5)
except MyError as e:
    print("User-defined exception:", e)



# 7. Practical example: Opening a File
# -----------------------------------------------------------------------------------------------
try:
    with open("file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist.")



# 8. Practical example: User input validation
# -----------------------------------------------------------------------------------------------
def get_positive():
    while True:
        try:
            x = int(input("Enter a positive number: "))
            if x <= 0:
                raise ValueError("Must be greater than 0")
            return x
        except ValueError as e:
            print("Error:", e)

num = get_positive()
print("You entered:", num)










# -----------------------------------------------------------------------------------------------
# ZeroDivisionError: Occurs when dividing by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# -----------------------------------------------------------------------------------------------
# ValueError: Invalid value conversion or wrong value
try:
    num = int("abc")
except ValueError:
    print("Invalid literal for int()")
# -----------------------------------------------------------------------------------------------
# TypeError: Operation between incompatible types
try:
    result = '2' + 3
except TypeError:
    print("Cannot add str and int")
# -----------------------------------------------------------------------------------------------
# FileNotFoundError: Trying to open a file that does not exist
try:
    with open("nofile.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
# -----------------------------------------------------------------------------------------------
# IndexError: Accessing an invalid index in a sequence
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range.")
# -----------------------------------------------------------------------------------------------
# KeyError: Dictionary key does not exist
try:
    d = {'a': 1}
    print(d['b'])
except KeyError:
    print("Key not found in dictionary.")
# -----------------------------------------------------------------------------------------------
# AttributeError: Accessing a non-existent attribute
try:
    s = "hello"
    s.append('!')
except AttributeError:
    print("Object has no attribute 'append'.")
