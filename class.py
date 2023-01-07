#!/usr/bin/python3

class myClass:
    color = "red"

a_class = myClass()
print(a_class.color)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("My name is " + self.name)

person1 = Person("Joanne", 32)
person2 = Person("Jane", 29)
print(person1.age)
print(person2.name)
print(person2.myfunc())
person1.age = 31
print(person1.age)


"""without the __str__ function"""
print(person1) # <__main__.Person object at 0x7fb64f460340>

""" with __str__ function """
class Dog:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        return f"My name is {self.name} and I am {self.colour}"

dog1 = Dog("Barry", "black")
print(dog1)

""" pass is used when you have a clas with no content, so as to prevent an error"""
class usingPass:
    pass
