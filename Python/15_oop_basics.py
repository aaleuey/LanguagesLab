# 1. Class Definition and Object Creation
# -----------------------------------------------------------------------------------------------
class Person:
    pass

p = Person()     # Create an object (instance)
print(type(p))   # <class '__main__.Person'>



# 2. Constructor (`__init__`)
# -----------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

p1 = Person("Hana", 21)
print(p1.name, p1.age)   # Hana 21

# `self` is a keyword that refers to the instance (the object itself).



# 3. Instance Method
# -----------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hi, I'm {self.name}.")

p1 = Person("Hana")
p1.greet()  # Hi, I'm Hana.



# 4. Attributes vs Methods
# -----------------------------------------------------------------------------------------------
class Hamster:
    def __init__(self, name):
        self.name = name   # attribute

    def squeak(self):      # instance method
        print("Squeak!")

h = Hamster("Maro")
print(h.name)  # Maro
h.squeak()     # Squeak!



# 5. Creating Multiple Objects
# -----------------------------------------------------------------------------------------------
p1 = Person("Hana", 21)
p2 = Person("Hoyoung", 25)

p1.greet()
p2.greet()

# Each object has its own independent state.



# 6. `__str__` Method
# -----------------------------------------------------------------------------------------------
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Factfulness")
print(b)  # Book: Factfulness

# The method taht is automatically called when an object is printed as as tring.



# 7. Class Variable vs Instance Variable
# -----------------------------------------------------------------------------------------------
class Student:
    university = "RWTH Aachen"  # Class variable

    def __init__(self, name, major):
        self.name = name      # Instance variable
        self.major = major

s1 = Student("Hana", "Computer Science")
s2 = Student("Hoyoung", "Cybersecurity")

print(s1.university)       # RWTH Aachen
print(Student.university)  # Accessing class variable via class

print(s1.name)  # Hana
print(s1.major) # Computer Science
print(s2.name)  # Hoyoung
print(s2.major) # Cybersecurity



# 8. Passing Arguments in a Method
# -----------------------------------------------------------------------------------------------
class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()
print(c.add(3, 5))   # 8



# 9. A simple practical Example of Object-Oriented Programming
# -----------------------------------------------------------------------------------------------
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def show(self):
        print(f"{self.name}'s balance: ${self.balance}")

a1 = Account("Hana", 10000)
a1.deposit(5000)
a1.show()  # Hana's balance: $15000



# 10. The four core prinsiples of Object-Oriented Programming (OOP 4 Pillars)
# -----------------------------------------------------------------------------------------------
'''
| Principle     | Explanation                                           |
|---------------|-------------------------------------------------------|
| Abstraction   | Hides complexity and exposes only what is necessary   |
| Encapsulation | Protects and hides data (e.g., self.__variable)       |
| Inheritance   | Code reuse by extending a parent class (covered next) |
| Polymorphism  | Enables different behaviors with the same method name |
'''
