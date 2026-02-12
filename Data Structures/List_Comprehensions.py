#without using list comprehension 

list=[]
for i in range(1,11):
    list.append(i**2)
print(list)

# using list comprehension
list=[i**2 for i in range(1,11)]
print(list)


# list of tuples with number and its square
[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]