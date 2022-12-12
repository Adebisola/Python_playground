#!/usr/bin/python3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

b = '''Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.'''
print(a)
print(b)
c = "Python is god"
for x in c:
    print(x)
print(len(c))

string = "Football is life"
print("life" in string)
if ("life" in string):
    print("Yes, Football is life")

txt = "The best things in life are free"
if ("expensive" not in txt):
    print("Life is beautiful")
print("expensive" not in txt)
