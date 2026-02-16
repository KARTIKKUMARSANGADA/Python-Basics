#try:it is used to wrap a block of code that may raise an exception. If an exception occurs within the try block, the program will jump to the except block to handle the exception instead of crashing.

#except:here it is used to catch and handle exceptions that may occur in the try block. It allows us to write code that can gracefully handle errors without crashing the program.

#pass:it is used when we want to write code later or when we want to create a function that does nothing. It does not show error but pass it without any implementation.

#raise: for generating exceptions manually at a particular point in the code.


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"The result of {a} divided by {b} is: {result}")
        
#try statement has more except blocks to handle different types of exceptions. 

        
def add(a, b):
    pass

#now if we call add(2, 3) it will not do anything because we have used pass statement which does not shows error but pass it without any implementation. It is used when we want to write code later or when we want to create a function that does nothing.


# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")
    

# In this code, we are using the raise statement to manually raise a ValueError if the age is negative. This allows us to enforce certain conditions in our code and provide meaningful error messages when those conditions are not met.




try:
    input = int(input("Enter your number: "))
    if input < 18:
        raise ValueError("Age cannot be less than 18")
    print(f"You entered: {input} and eligible for voting.")
except ValueError as e:
    print(e)
# In this code, we are using a try-except block to handle exceptions. We are trying to convert the user input to an integer and check if it is less than 18. If it is, we raise a ValueError with a custom error message. The except block catches this exception and prints the error message to the user.


try:
    name  = input("Enter your name: ")
    if not name.isalpha():
        raise ValueError("Name must contain only letters.")
    print(f"Hello, {name}!")
except ValueError:
    print("Invalid name. Please enter a name that contains only letters.")    
