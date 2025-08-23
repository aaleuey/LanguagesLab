# 1. Tuple
# -----------------------------------------------------------------------------------------------
# Creation and Usage
t = (1, 2, 3)
print(t[0])       # 1

# Featrues: Ordered (supports indexing), Immutable (cannot be changed)
t[0] = 10   # ❌ TypeError

# Unpacking (Assigning to Multiple Variables)
a, b, c = (1, 2, 3)
print(a, b, c)



# 2. Dictionary
# -----------------------------------------------------------------------------------------------
# Creation
person = {
    "name": "Hana",
    "age": 21
}

# Read / Update / Create / Delete
print(person["name"])  
person["age"] = 25
person["job"] = "developer"
del perseon["age"]

# Method
print(person.keys())       # dict_keys(['name', 'job'])
print(person.values())     # dict_values(['Daa', 'developer'])
print(person.items())      # dict_items([('name', 'Daa'), ('job', 'developer')])

# Safe Access: `get()`
print(person.get("address", "Not available"))   # Returns default value if key is missing

# Using Loops
for key, value in person.items():
    print(f"{key}: {value}")



# 3. Set
# -----------------------------------------------------------------------------------------------
# Creation
s = {1, 2, 3, 2, 1}
print(s)   # {1, 2, 3} ← duplicates are removed

# For Removing Duplicates
names = ["Hana", "Hoyoung", "Hana", "Maro"]
unique_names = list(set(names))

'''
Sets are unordered collections, so the element order is not guaranteed.
Because sets are unordered, the output order may change.
'''

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union -> {1, 2, 3, 4, 5}
print(a & b)   # Intersection -> {3}
print(a - b)   # Difference (elements in a but not in b) -> {1, 2}
print(a ^ b)   # Symmetric difference (elements in a or b but not both) -> {1, 2, 4, 5}
