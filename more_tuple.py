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


