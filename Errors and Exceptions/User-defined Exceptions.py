# User-defined exceptions are errors that you create yourself when Python’s built-in exceptions are not enough for your program.

# To create a user-defined exception, you need to define a new class that inherits from the built-in Exception class. You can also add your own attributes and methods to this class if needed.

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
try:
    raise CustomError("This is a custom error message") # This will raise an instance of the CustomError with the specified message 
except CustomError as e:
    print(f"Caught an exception: {e.message}") # This will catch the CustomError and print the message associated with it   
    
    