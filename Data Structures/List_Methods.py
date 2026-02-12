List = ["Apple", "Banana", "Cherry"]

# Append() method adds an element at the end of the list
List.append("Orange")
print(List)

# extend() method adds all the elements of an iterable (list, tuple, etc.) to the end of the list you can add multiple elements at once using extend() method
List.extend(["Grapes", "Pineapple"])
print(List)

# Insert() method adds an element at the specified position
List.insert(1, "Mango")
print(List)

# Remove() method removes the specified element from the list
List.remove("Banana")
print(List)

# Pop() method removes the element at the specified position
List.pop(2)
print(List)

# # Clear() method removes all the elements from the list
# List.clear()
# print(List)


# returns the number of times the specified element appears in the list
List.count("Apple")  
print(List.count("Apple"))

# returns the index of the first element with the specified value
print(List.index("Mango")) 

# Sorts the list in ascending order if we have to descending order then we can use sort(reverse=True)
List.sort(reverse=True )
print(List)

# creates a copy of the list
a =List.copy() 
print(a)    





