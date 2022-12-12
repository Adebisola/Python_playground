#!/usr/bin/python3
x = "awesome"

def myfunc():
    x = "cool"
    print("Python is " + x)
myfunc()

print("Python is " + x)

# create a global scope in a function
def func():
    global y
    y = "fantastic"
func()
print("Python is a " + y + " language")


# use global keyword to change a global variable inside a function
a = "life"
def yourfunc():
    global a
    a = "incredible"
yourfunc()
print("Python is " + a)
