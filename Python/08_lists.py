# 1. List creation and print
# -----------------------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits)



# 2. Indexing and Slicing
# -----------------------------------------------------------------------------------------------
print(fruits[0])      # 'apple' (first element)
print(fruits[-1])     # 'cherry' (last element)
print(fruits[1:3])    # ['banana', 'cherry'] (elements from index 1 to 2)
print(fruits[::-1])   # reverse the list



# 3. Lists are Mutable (Values Can Be Changed)
# -----------------------------------------------------------------------------------------------
fruits[0] = "grape"
print(fruits)   # ['grape', 'banana', 'cherry']



# 4. Summary of Key Methods
# -----------------------------------------------------------------------------------------------
numbers = [1, 11, 19, 2024, 1]

numbers.append(2)         # Add 2 to the end
numbers.insert(1, 99)     # Insert 99 at index 1
numbers.remove(1)         # Remove the first occurrence of 1
numbers.pop()             # Remove the last element
numbers.sort()            # Sort in ascending order
numbers.reverse()         # Reverse the list
print(numbers)



# 5. Length, sum, Maximum/Minimum
# -----------------------------------------------------------------------------------------------
nums = [11, 19, 2024, 2]
print(len(nums))     # 4
print(sum(nums))     # 2056
print(max(nums))     # 2024
print(min(nums))     # 2



# 6. Checking for Membership (`in` Operator)
# -----------------------------------------------------------------------------------------------
print("banana" in fruits)      # True
print("mango" not in fruits)   # True



# 7. Using with Loops
# -----------------------------------------------------------------------------------------------
for fruit in fruits:
    print(fruit)    # Print each fruit in the list

# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)  # Print index and fruit



# 8. List Comprehension (List Embedding)
# -----------------------------------------------------------------------------------------------
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]



# 9. Nested Lists
# -----------------------------------------------------------------------------------------------
matrix = [[1, 2], [3, 4]]

print(matrix[0])      # [1, 2]
print(matrix[0][1])   # 2



# 10. List Copy - Shallow Copy vs Deep Copy
# -----------------------------------------------------------------------------------------------
a = [1, 2, 3]
b = a         # Shallow copy (shares the same reference)
b[0] = 99
print(a)      # [99, 2, 3]

# To make a true copy
c = a[:]      # Copy by slicing
d = list(a)   # Copy using list()
import copy
e = copy.deepcopy(a)   # Deep copy
