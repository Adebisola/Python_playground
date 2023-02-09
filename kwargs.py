#!/usr/bin/python3

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="Joke", age=44, sex="female")


def print_kwargsDict(**kwargs):
    for key,value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_kwargsDict(my_name = "Moni", your_name = "Bayo")
