#!/usr/bin/python3

fruits = ("apple","orange","banana")
(red,yellow,green) = fruits
print(red)
print(yellow)
print(green)

animals = ("elephant","shark","octopus","whale")
(land, *sea) = animals
print(land)
print(sea)

fruit = ("apple","watermelon", "papaya","guava","strawberry","berry", "banana")
(red, *others, green) = fruit
print(red)
print(others)
print(green)

for x in fruit:
    print(x)

for y in range(len(fruits)):
        print(fruits[y])

i = 0
while i < len(animals):
    print(animals[i])
    i = i + 1

multiply_tuple = animals * 2
print(multiply_tuple)

count = multiply_tuple.count("elephant")
print(count)
index = multiply_tuple.index("elephant")
print(index)
