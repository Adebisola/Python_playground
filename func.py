#!/usr/bin/python3

def myfunc():
    print("This is a function")
myfunc()

def myname(name):
    print("My name is "+ name)
myname("Tobi")

def my_func(fname, lname):
    print(fname + " " + lname)
my_func("Borja", "Hamidu")

""" when you are unsure of the number of args, it receives a tuple"""
def family(*kids):
    print("The oldest kid in the family is " + kids[3])

family("Bolaji","Bolanle", "Kofo","Gbemi","Lade")


""" this function receives keyword args"""
def fam(child1, child2, child3):
    print("The youngest child is " + child2)
fam(child1 = "bose", child2 = "wale", child3 ="lolade")


""" kwargs, this function receives a dict of args"""
def a_func(**myname):
    print("My name is " + myname["lname"])
a_func(fname = "Tomas", lname = "Romano")


""" default parameter value"""

def our_function(country = "Colombia"):
    print("I am from " + country)

our_function("India")
our_function("Jamaica")
our_function("Ghana")
our_function()

""" passing a list to a function """

def this_func(food):
    for x in food:
        print(x)
fruits = ["mango", "apple", "banana"]

this_func(fruits)

def multiply(y):
    return 5 * y
print(multiply(40))
print(multiply(16))
print(multiply(24))


def add(x):
    return 10 * x

print(add(6))

print(add(14))


def empty_function():
    pass



