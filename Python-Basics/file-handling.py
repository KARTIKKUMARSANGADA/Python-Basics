
# File handling in python
# writing to a file
with open ("demo.txt", "w") as f:
    f.write("this is demo file \n")

    
    
# reading from a file 
with open ("demo.txt", "r") as f:
    data = f.read()
    print(data)
   
    
# appending to a file
with open ("demo.txt", "a") as f:
    f.write("this is appended data \n")
    
    
