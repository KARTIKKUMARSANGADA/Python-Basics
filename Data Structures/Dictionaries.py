dict = {
    'name': 'kartik',
    'age': 22,
    'course': 'python',
    'hobbies': ['coding', 'gaming', 'traveling']
}

print(dict)
# to find the type of the dictionary we can use the type() function
print(type(dict))

# to access the keys of the dictionary we can use the keys() method
print(dict.keys())
for key in dict:
    print(key)

# to access the values of the dictionary we can use the values() method
print(dict.values())
for value in dict.values():
    print(value)
    
# we can also access the values using the keys 
print(dict['name'])
print(dict['age'])

# to add a new key-value pair in the dictionary we can simply assign a value to a new key
dict['name'] = 'parth'
print(dict)


# to delete a key-value pair from the dictionary we can use del keyword
del dict['course']
print(dict) 





