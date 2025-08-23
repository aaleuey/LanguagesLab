# 1. Arithmetic Operators
# -----------------------------------------------------------------------------------------------
a = 10
b = 3

print(a + b)    # 13 (addition)
print(a - b)    # 7  (subtraction)
print(a * b)    # 30 (multiplication)
print(a / b)    # 3.333... (division, float result)
print(a // b)   # 3  (floor division, integer quotient)
print(a % b)    # 1  (modulus, remainder)
print(a ** b)   # 1000 (exponentiation)



# 2. Assignment Operators
# -----------------------------------------------------------------------------------------------
x = 5
x += 3   # x = x + 3 -> 8
x *= 2   # x = x * 2 -> 16
x -= 4   # x = x - 4 -> 12



# 3. Comparison Operators
# -----------------------------------------------------------------------------------------------
print(3 == 3)   # True (equal)
print(4 != 5)   # True (not equal)
print(5 > 2)    # True
print(3 <= 2)   # False



# 4. Logical Operators
# -----------------------------------------------------------------------------------------------
a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False



# 5. Membership Operators (`in`, `not in`)
# -----------------------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("grape" not in fruits)   # True



# 6. Identity Operators (`is`, `is not`)
# -----------------------------------------------------------------------------------------------
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)    # True  (values are equal)
print(x is y)    # False (different objects)
print(x is z)    # True  (same object)



# 7. Bitwise Operators
# -----------------------------------------------------------------------------------------------
a = 5   # 0b0101
b = 3   # 0b0011

print(a & b)    # 1  (AND)
print(a | b)    # 7  (OR)
print(a ^ b)    # 6  (XOR)
print(~a)       # -6 (NOT, two's complement)
print(a << 1)   # 10 (Left shift)
print(a >> 1)   # 2  (Right shift)



# 8. Priority of Operators
# -----------------------------------------------------------------------------------------------
result = 3 + 2 * 4     # 11 (multiplication happens first)
result = (3 + 2) * 4   # 20



# 9. Using Conditional Expressions (Ternary Operators)
# -----------------------------------------------------------------------------------------------
age = 21
result = "Adult" if age >= 18 else "Minor"
print(result)   # Adult
