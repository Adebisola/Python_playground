#!/usr/bin/python3

def multiply(*args):
    product = 1
    for num in args:
        product *= num
    print(product)

multiply(2,5,10)
multiply(16,5)
multiply(5,6,8)
