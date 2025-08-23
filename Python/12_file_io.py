# 1. Opening a File
# -----------------------------------------------------------------------------------------------
f = open("example.txt", "w")   # Open the file in write mode
f.write("Hello, file!")        # Write text to the file
f.close()                      # Close the file

'''
"r"  Read mode (default)
"w"  Write mode (overwrites existing file)
"a"  Append mode (adds content to end of file)
"x"  Exclusive creation (fails if file exists)
"b"  Binary mode (read/write in binary format)
"t"  Text mode (default, read/write as text)

example mode combinations
"rb"  Read in Binary mode
"wt"  Write in Text mode
"ab"  Append in Binary mode
'''



# 2. Reading a File
# -----------------------------------------------------------------------------------------------
f = open("example.txt", "r")   # Open the file in read mode
content = f.read()             # Read the entire contents of the file
print(content)                 # Print the contents to the screen
f.close()                      # Close the file



# 3. Using the `with` statement (automatically closes the file)
# -----------------------------------------------------------------------------------------------
with open("example.txt", "r") as f:
    text = f.read()
    print(text)
# `f.close()` is automatically called after this block



# 4. Reading line by line
# -----------------------------------------------------------------------------------------------
with open("multi_line.txt", "r") as f:
    lines = f.readlines()  # Read all lines into a list

for line in lines:
    print(line.strip())    # Remove newline character at the end and print each line
'''
or
'''
with open("multi_line.txt") as f:
    for line in f:
        print(line, end="")  # Print each line as is without adding extra newline



# 5. Writing a File (Overwriting/Appeding)
# -----------------------------------------------------------------------------------------------
# Overwriting
with open("write_test.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Appending
with open("write_test.txt", "a") as f:
    f.write("Third line\n")



# 6. Storing user input in a File
# -----------------------------------------------------------------------------------------------
with open("user_input.txt", "w") as f:
    while True:
        line = input("Enter text (type 'q' to quit): ")
        if line == "q":
            break
        f.write(line + "\n")



# 7. `"w+"`, `"r+"`, `"a+"` mode (Read + Write)
# -----------------------------------------------------------------------------------------------
with open("sample.txt", "w+") as f:
    f.write("Hello\n")
    f.seek(0)        # Move the cursor back to the beginning
    print(f.read())  # Reading is possible after writing

'''
"w+"  Write and Read mode (overwrites existing file)
"r+"  Read and Write mode (file must exist)
"a+"  Append and Read mode (writes appended at end)
'''



# 8. Text vs Binary
# -----------------------------------------------------------------------------------------------
# Text mode
with open("text.txt", "wt") as f:
    f.write("hello")

# Binary mode
with open("img.jpg", "rb") as f:
    data = f.read()



# 9. Using with Exception Handling
# -----------------------------------------------------------------------------------------------
try:
    with open("not_exist.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist.")
