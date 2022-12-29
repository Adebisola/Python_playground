#!/usr/bin/python3

car = {
        "brand": "volvo",
        "color": "blue",
        "year" : 2008,
        "num_of_doors" : 2
        }
""" this prints the key"""
for x in car:
    print(x)

for y in car:
    print(car[y])
""" prints the values"""
for a_car in car.values():
    print(a_car)
"""prints the keys"""
for a_key in car.keys():
    print(a_key)

""" prints the values and the keys"""
for a, b in car.items():
    print(a, b)



_car2 = car.copy()
print(_car2)

_car3 = dict(_car2)
print(_car3)
