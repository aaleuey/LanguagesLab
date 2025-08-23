# 1. Basic structure of Inheritance
# -----------------------------------------------------------------------------------------------
class Animal:        # Parent class (Super Class)
    def speak(self):
        print("The animal makes a sound.")

class Hamster(Animal):   # Child class (Sub Class)
    def squeak(self):
        print("Squeak!")

h = Hamster()
h.speak()    # Method inherited from Animal
h.squeak()   # Hamster's own method



# 2. Constructor Overriding and `super()`
# -----------------------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

class Hamster(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

h = Hamster("Maro", "Golden hamster")
print(h.name, h.breed)

'''
`super().__init()` is a function that calls the constructor of the parent class.
It's not mandatory, but it's a good practice to call it explicitly.
'''



# 3. Method Overriding (Redefinition)
# -----------------------------------------------------------------------------------------------
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

a = Animal()
c = Cat()

a.speak()   # Animal sound
c.speak()   # Meow! (overridden)

'''
A method with the same name can be redefined in the child class.
'''



# 4. Multiple Inheritance
# -----------------------------------------------------------------------------------------------
class Flyable:
    def fly(self):
        print("Can fly")

class Bird(Animal, Flyable):   # Inherits from both Animal and Flyable
    pass

b = Bird("Sparrow")
b.speak()        # Inherited from Animal
b.fly()          # Inherited from Nocturnal

'''
Python supports multiple inheritance, but clear separation of responsibilities is important.
'''



# 5. `isinstance` and `issubclass`
# -----------------------------------------------------------------------------------------------
print(isinstance(h, Hamster))   # True
print(isinstance(h, Animal))    # True

print(issubclass(Hamster, Animal))   # True



# 6. Practical Example
# -----------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
    
    def info(self):   # Overriding
        super().info()
        print(f"Major: {self.major}")

s = Student("Hana", "Computer Science")
s.info()



# 7. `protected`/`private` Attributes (_, __)
# -----------------------------------------------------------------------------------------------
class Parent:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"

p = Parent()
print(p._protected)         # Not recommended, but possible
# print(p.__private)        # Error
print(p._Parent__private)   # Can access via name mangling (not recommended)



# 8. Class Structure Summary
# -----------------------------------------------------------------------------------------------
class A:
    def show(self): print("A")

class B(A): pass
class C(A): pass
class D(B, C): pass

d = D()
d.show()  # A -> according to MRO (Method Resolution Order)
