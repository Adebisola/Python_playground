#!/usr/bin/python3
a_set = {"woman", "boy","girl","man"}
print(type(a_set))
print(len(a_set))
this_set = set((True, 28, "dinosarus", 3.9))
print(this_set)

for x in a_set:
    print(x)

print("boy" in a_set)

a_set.add("baby")
print(a_set)
new_set = a_set.update(this_set)
print(new_set)
a_list = ["thanks", "danke"]
this_set.update(a_list)
print(this_set)
