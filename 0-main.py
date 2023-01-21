#!/usr/bin/python3

import mymodule as mx
import platform

mx.greetings("Johnson")

x = mx.person1["country"]
print(x)

y = mx.person1["name"]
print(y)

a = platform.system()
print(a)

b = dir(mx)
print(b)
