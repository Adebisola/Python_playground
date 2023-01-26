#!/usr/bin/python3
""" "r" - read- default: opens file for reading, error if files does not exist
    "a" - append- open file for appending, creates the file if it does not exist
    "w" - write to a file, create if it does not exist.
    "x" - creates a new file, error if it exists already.
    "t" - text mode(default) - texts.
    "b" - binary mode(Images)
"""
f = open("demofile.txt", "r")
##print(f.read())
##print(f.read(5))
##print(f.readline())
##print(f.readline())
for x in f:
    print(x)
f.close()
text = open("demofile2.txt", "a")
text.write("Now this file has new content")
text.close()

text = open("demofile2.txt", "r")
print(text.read())

text = open("demofile2.txt", "w")
text.write("Yes, I can overwrite the content")
text.close()

text = open("demofile2.txt", "r")
print(text.read())

