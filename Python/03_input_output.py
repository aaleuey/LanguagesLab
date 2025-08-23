# 1. Basic Input and Output
# -----------------------------------------------------------------------------------------------
name = input("What is your name? ")
message = "hi, " +name+ ". nice to meet you ... bye, " +name+ "."
print(message)



# 2. Input is Always a String
# -----------------------------------------------------------------------------------------------
age = input("How old are you? ")
print(type(age))  # <class 'str'>



# 3. Converting Input to a Number (Type Casting)
# -----------------------------------------------------------------------------------------------
age = int(input("Enter your age: "))
year = 2025 - age + 100
print(f"You will turn 100 years old in the year {year}.")



# 4. Getting Multiple Inputs (Using split)
# -----------------------------------------------------------------------------------------------
# Getting multiple inputs in one line
a, b = input("Enter two numbers separated by space: ").split()
a, b = int(a), int(b)
print(f"Sum: {a + b}")



# 5. Converting Input in One Line Using `map()`
# -----------------------------------------------------------------------------------------------
# Getting multiple numbers as a list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Numbers entered: ", numbers)



# 6. Reading Multiple Lines of Input (Using `for` + `input()`)
# -----------------------------------------------------------------------------------------------
print("Enter 3 lines: ")
lines = []
for _ in range(3):
    line = input()
    lines.append(line)

print("You entered: ")
print("\n".join(lines))



# 7. `f-string` Formatting
# -----------------------------------------------------------------------------------------------
name = "Hana"
score = 95.72

print(f"{name}'s score is {score:.2f}.")   # Rounded to 2 decimal places



# 8. Table-formatted Output Alignment (`rjust`, `ljust`, `center`)
# -----------------------------------------------------------------------------------------------
print("name".ljust(10), "score".rjust(5))
print("Hana".ljust(10), str(95).rjust(5))



# 9. Automatic Output Without Input
# -----------------------------------------------------------------------------------------------
# How to add a delay when printing automatically
import time

print("3")
time.sleep(1)   # Wait for 1 second
print("2")
time.sleep(1)   # Wait for 1 second
print("1")



# Using with Exception Handling
# -----------------------------------------------------------------------------------------------
try:
    x = int(input("Enter an integer: "))
    print(f"The square of x is: {x**2}")
except ValueError:
    print("That's not a valid number.")
