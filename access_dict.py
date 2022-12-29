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

