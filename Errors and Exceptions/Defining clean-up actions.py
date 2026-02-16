# “Defining clean-up actions” in Python usually means using the finally block
# A clean-up action is code that must run no matter what happens — whether an error occurs or not.

try:
    # Code that may raise an exception
    result = 10 / 0  
    print(result)          # This will raise a ZeroDivisionError  
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
finally:    # This block will always execute, even if an error occurs
    print("This is a clean-up action that runs regardless of errors.")  
    
# In this example, the finally block will execute after the except block, ensuring that the clean-up action is performed even if an error occurs.

try:
    f = open("example.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    
    
    
try:
    f.close()  # This will raise an error if the file was never opened
except NameError:
    print("File was never opened")
finally:
    print("Finished attempting to close the file")
    

try:
    result = 10 / 0
except ZeroDivisionError:   
    print("Cannot divide by zero")
else:
    print("Division successful, result is:", result)
finally: 
    print("This will always execute, even if an error occurs.")
    
