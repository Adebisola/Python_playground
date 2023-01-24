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
    pass

Student = Person1("Bolanle", "Ajadi")
Student.printname()
