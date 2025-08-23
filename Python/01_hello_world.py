# 1. Basic Output
# -----------------------------------------------------------------------------------------------
print("Hello, World!")  # Hello, World!



# 2. Several Values Output
# -----------------------------------------------------------------------------------------------
print("Hello", "Python", "World")  # Hello Python World



# 3. `sep` (separator), `end` (end of line)
# -----------------------------------------------------------------------------------------------
print("apple", "banana", "cherry", sep=" | ")  # apple | banana | cherry

print("line1", end=" ")  # line1 line2
print("line2")  



# 4. Escape Character
# -----------------------------------------------------------------------------------------------
print("I said, \"Hello\"")  # \"
print("First line\nSecond line")  # \n
print("Item\tPrice")  # \t



# 5. Format Strings in Python
# -----------------------------------------------------------------------------------------------
name = "Hana"
age = 21

# 1: % format
print("My name is %s and I am %d years old." % (name, age))

# 2: .format()
print("My name is {} and I am {} years old.".format(name, age))

# 3: f-string
print(f"My name is {name} and I am {age} years old.")
