#!/usr/bin/python3
print(10 > 8)
print(10 == 9)
print(10 < 9)
a = 250
b = 349
if a < b:
    print("b is greater than a")
else:
    print("a is greater than b")

print(bool("Hello"))
print(bool(17))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction():
    return True
print(myFunction())

def myFunc():
    return True

if myFunction():
    print("YES")
else:
    print("NO")

x = 200
print(isinstance(x, int))
