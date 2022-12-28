#!/usr/bin/python3

a_tuple = (23,14,19,60)
print(type(a_tuple))
b_tuple = tuple((True,False,True))
print(b_tuple)

print(a_tuple[1:3])
print(a_tuple[:3])
print(b_tuple[:])
print(b_tuple[-2])

if 14 in a_tuple:
    print("Yes")

this_tuple = ("Lagos","Oyo","Osun","Ondo","Ebonyi")
a_list = list(this_tuple)
a_list[-1] = "Ekiti"
this_tuple = tuple(a_list)
print(this_tuple)

y = list(this_tuple)
y.append("Ogun")
this_tuple = tuple(y)
print(this_tuple)
a = ("Abuja",)
this_tuple += a
print(this_tuple)
