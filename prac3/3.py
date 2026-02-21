#1
class Student:
    name = "Default Name"
    old = "18"

s1 = Student()

print(s1.name + " " + s1.old)

#2
class Student:
    def __init__(self, name, old):
        self.name = name
        self.old = old
s1 = Student("Dias", "18")
print(s1.name + " " + s1.old)

#3
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
name=input()
species=input() 
a1 = Animal(name, species)
print(a1.name + " is a " + a1.species)

#4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
radius = float(input())
c1 = Circle(radius)
print("Area of the circle:", c1.area())