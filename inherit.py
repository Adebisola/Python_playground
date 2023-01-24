#!/usr/bin/python3

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

myName = Person("Sola", "Akinsote")
myName.printname()

class Person1(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.age = 34
        self.graduationyear = year
    
    def welcome(self):
        print("Hello",self.firstname,self.lastname,"Welcome to the class of",self.graduationyear) 


Student = Person1("Bolanle", "Ajani", 2022)
Student.printname()
print(Student.graduationyear)
print(Student.age)
Student.welcome()
