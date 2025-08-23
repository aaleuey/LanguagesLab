# 1. Basic for Loop
# -----------------------------------------------------------------------------------------------
for i in range(5):
    print(i)

'''
range(5) generates numbers 0 through 4.
The loop variable i takes each value in that range and prints it.
'''



# 2. How to Use `range()`
# -----------------------------------------------------------------------------------------------
print(list(range(3)))          # [0, 1, 2]
print(list(range(2, 6)))       # [2, 3, 4, 5]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]



# 3. `while` Loop
# -----------------------------------------------------------------------------------------------
count = 0
while count < 3:
    print("Hi")
    count += 1



# 4. `break` and `continue`
# -----------------------------------------------------------------------------------------------
for i in range(5):
    if i == 3:
        break      # Stop the loop at 3

for i in range(5):
    if i == 3:
        continue   # Skip 3
    print(i)



# 5. Nested Loops
# -----------------------------------------------------------------------------------------------
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")



# 6. String/List Loop
# -----------------------------------------------------------------------------------------------
for char in "python":
    print(char)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)



# 7. Dictionary Loop
# -----------------------------------------------------------------------------------------------
person = {"name": "Hana", "age": 21}

for key in person:
    print(key, ":", person[key])

# More explicit way
for k, v in person.items():
    print(f"{k} : {v}")



# 8. Using `enumerate()` to access index and value together
# -----------------------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)



# 9. `for + else` Pattern (Uncommon but Useful!)
# -----------------------------------------------------------------------------------------------
for n in range(2, 10):
    if n % 7 == 0:
        print("Multiple of 7 found:", n)
        break
else:
    print("No multiples of 7 found")



# 10. Using `zip()` to loop through two lists at once
# -----------------------------------------------------------------------------------------------
names = ["Hana", "Hoyoung", "Maro"]
scores = [95, 96, 97]

for name, score in zip(names, scores):
    print(f"{name} : {score}")
