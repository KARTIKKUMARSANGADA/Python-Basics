import json
x = [1, 'kartik', 'python']
print(json.dumps(x))
# json.dumps() is a method that converts a Python object into a JSON string.

with open('example.json', 'a') as file:
    json.dump(x, file)  # json.dump() is a method that writes a Python object to a file in JSON format.


# to read the data from the file we can use json.load() method
# to save the data in a file we can use json.dump() method
# to convert a Python object into a JSON string we can use json.dumps() method
# to convert a JSON string into a Python object we can use json.loads() method 

