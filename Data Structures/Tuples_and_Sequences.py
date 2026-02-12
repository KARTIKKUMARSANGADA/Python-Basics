tuple = ("Apple", "Banana", "Cherry")

tuple2 = "grapes", "Pineapple", "Mango"

tuple3 = tuple + tuple2
print(tuple3)     


a,b,c = tuple
print(a)
print(b)
print(c)

# you can also create a tuple without using parentheses, just by separating the values with commas. by default it will be considered as a tuple

# count() method returns the number of times the specified element appears in the tuple
print(tuple.count("Apple"))

# index() method returns the index of the first element with the specified value
print(tuple.index("Banana"))
