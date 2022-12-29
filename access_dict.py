#!/usr/bin/python3
physio = {
        "name": "Berbakaz",
        "address" : "Ikirun",
        "qualification": "BMR"
        }
""" this prints the value of the key"""
print(physio["name"])

"""prints the value of the key"""
x = physio.get("address")
print(x)

""" returns a list of the keys in the dictionary"""
y = physio.keys()
print(y)
physio["rotation"] = "medicine"
print(y)

""" returns a list of all the values in the dict."""
my_values = physio.values()
print(my_values)
physio["rotation"] = "cardiopulmonary"
print(physio)

"""returns each item in a dict as tuples in a list"""

get_items = physio.items()
print(get_items)

if("name" in physio):
    print("Yes, I know the name of my physio")

physio.update({"school":"Univeristy of Ibadan"})
print(physio)
a_dict = {
        "animal": "cow",
        "name" : "banny",
        "legs" : 4
        }
""" removes the specified key and its value(the item)"""
a_dict.pop("name")

"""popitem() removes the last inserted item"""
a_dict.popitem()
print(a_dict)

