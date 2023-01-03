#!/usr/bin/python3

addition = lambda a : a + 20
print(addition(5))

multiply = lambda a, b : a * b
print(multiply(6,10))

add_string = lambda str1, str2 : str1 + " "  + str2
print(add_string("Lowe", "Brown"))


sum = lambda a, b, c : a + b + c
print(sum(4,8,12))


def myfunc(n):
    return lambda a : a * n

double_num = myfunc(2)
print(double_num(11))

def a_func(n):
    return lambda a : a * n

triple_num = a_func(3)
print(triple_num(22))


def b_func(n):
    return lambda a : a * n

mydoubler = b_func(2)
mytripler = b_func(4)
print(mydoubler(6))
print(mytripler(10))

