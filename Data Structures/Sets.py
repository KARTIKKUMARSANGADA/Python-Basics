# it removes duplicates and it is unordered
myset = {1, 2, 3, 4, 5, 5, 5}
print(myset)

b=set("hdbfjshjafhjkahjha")
print(b)

# to add an element in set
myset.add(6)
print(myset)

# to remove an element in set
myset.remove(3)
print(myset)

# to check if an element is present in set
print(4 in myset)

# to find the length of set
print(len(myset))

# # to clear the set
# myset.clear()

# set comprehensions
myset2 = {x**2 for x in range(10)}
print(myset2)

