# Exception chaining in Python means linking one error to another error so you can see the original cause of a problem.
# This is useful when you catch an error and then raise a new one.

try:
    name=input("Enter your name: ")
    convert_name = int(name)  # This will raise a ValueError if the input is not a number
except ValueError as e:
    raise TypeError("Name must be a string") from e  # This raises a new TypeError and links it to the original ValueError

# In this example, if the user enters a non-numeric name, a ValueError will be raised. The except block catches this ValueError and raises a new TypeError, linking it to the original ValueError using the "from" keyword. This way, when the TypeError is raised, you can see the original ValueError that caused it.