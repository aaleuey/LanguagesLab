# 1. Ways to declare strings
# -----------------------------------------------------------------------------------------------
s1 = "Hello"
s2 = 'Python'
s3 = """This is
a multi-line string"""



# 2. String Indexing & Slicing
# -----------------------------------------------------------------------------------------------
text = "Python"

print(text[0])     # 'P'   (first character)
print(text[-1])    # 'n'   (last character)

print(text[1:4])   # 'yth' (characters from index 1 to 3)
print(text[:2])    # 'Py'  (characters from start to index 1)
print(text[::2])   # 'Pto' (every 2nd character)



# 3. Strings are Immutable
# -----------------------------------------------------------------------------------------------
text = "hello"
# text[0] = "H"  ❌ Error (strings are immutable)

text = "H" + text[1:]   # You must create a new string
print(text)   # 'Hello'



# 4. Common String Methods
# -----------------------------------------------------------------------------------------------
s = "  Hello Python!  "

print(s.lower())   # lowercase
print(s.upper())   # uppercase
print(s.strip())   # remove leading and trailing whitespace
print(s.replace("Python", "World"))   # replace substring
print(s.startswith("  He"))   # True  (starts with the given substring)
print(s.endswith("!  "))      # True  (ends with the given substring)



# 5. String Search
# -----------------------------------------------------------------------------------------------
s = "Data Science"

print("Sci" in s)       # True (checks if substring exists)
print(s.find("Sci"))    # 5 (returns the index, -1 if not found)
print(s.index("Sci"))   # 5 (returns the index, raises an error if not found)



# 6. String Splitting & Joining
# -----------------------------------------------------------------------------------------------
s = "apple, banana, cherry"
fruits = s.split(",")
print(fruits)   # ['apple', ' banana', ' cherry']

joined = " | ".join(fruits)
print(joined)   # apple |  banana |  cherry



# 7. String Sorting
# -----------------------------------------------------------------------------------------------
s = "42"
print(s.rjust(5))         # '   42'
print(s.ljust(5, '0'))    # '42000'
print(s.center(7, '-'))   # '--42---'



# 8. Unicode Characters and Emojis
# -----------------------------------------------------------------------------------------------
# Unicode characters
print("Hello, world! \u2600")      # Hello, world! ☀ (sun symbol)

# Emoji using Unicode
print("I love Python! 🐍")          # I love Python! 🐍

# Emoji with Unicode code point
print("Smiling face: \U0001F600")   # Smiling face: 😀
