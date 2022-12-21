#!/usr/bin/python3

a_list = [True, 10, "a string", 9.0, "orange", "banana","orange"]
list_type = type(a_list)
print("a_list is a type of {}".format(list_type))
print(len(a_list))

my_list = list(("Orange", "Apple", "Pineapple","Pear"))
print(my_list)
print(my_list[-3:-1])
if "Apple" in my_list:
    print("Yes, Apple is in the list")

my_list[2] = "Mango"
my_list.append("Guava")
my_list[3:5] = ["Watermelon", "Coconut"]
print(my_list)
my_list.insert(-1,"pawpaw")
print(my_list)
print(my_list[-1])
other_fruits = ["Pineapple", "Lemon", "Strawberries"]
my_list.extend(other_fruits)
print(my_list)
""" extend any iterables"""
a_tuple = ("kiwi", "Berries")
my_list.extend(a_tuple)
print(my_list)

b_list = [1,2,4,3,5]
b_list.remove(4)
print(b_list)
b_list.pop(1)
print(b_list)
c_list = [True, False, True]
c_list.clear()
print(c_list)
d_list = [2,3,4,5]
del d_list[1]
print(d_list)

""" my_list = [1,2,3,4,5]
[print(x) for x in my_list]
"""
