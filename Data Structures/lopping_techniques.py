List = [ "Apple", "Banana", "Cherry"]
dict = {
    'name': 'kartik',
    'age': 22,
    'course': 'python',
    'hobbies': ['coding', 'gaming', 'traveling']
}

# for loop to iterate through the dictionary
for key, values in dict.items():
    print(key, values)    
    
# to find the index of the element in the list we can use the enumerate() function
for i, fruit in enumerate(List):
    print(i, fruit)


# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
List1 = ["Apple", "Banana", "Cherry"]
List2 = [1, 2, 3]

for fruit, number in zip(List1, List2):
    print(f"at {number}. this is {fruit}")


# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for fruit in reversed(List1):
    print(fruit)