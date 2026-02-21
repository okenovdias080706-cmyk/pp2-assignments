#1
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()

#2
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Husky")

print(d.name)
print(d.breed)

#3
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()

#4
class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()