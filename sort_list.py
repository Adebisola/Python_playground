#!/usr/bin/python3
sort_list = ["Chelsea","Arsenal","Real Madrid","Porto"]
sort_list.sort()
print(sort_list)
sort_list.sort(reverse = True)
print(sort_list)


def myfunc(n):
    return abs(n-50)

a_list = [100,16,55,23,90,45]
""" this sorts the list based on how close
the number is t0 50
"""
a_list.sort(key = myfunc)
print(a_list)

cars = ["Volvo", "benz", "tesla", "Volkswagen", "Ford","mazda"]
cars.sort(key = str.lower)
print(cars)

cars.reverse()
print(cars)
