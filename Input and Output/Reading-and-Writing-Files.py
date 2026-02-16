
# writing into file 
file = open('example.json', 'w')  # open the file in write mode
file.write('Hello, world!\n')  # write a line to the file
file.write('This is a new line.\n')  # write another line to the file
file.close()  # close the file


# Reading from file
file=open('example.txt', 'r')  # open the file in read mode
content = file.read()  # read the entire content of the file
print(content)  # print the content of the file
file.close()  # close the file

# append to file
file = open('example.json', 'a')  # open the file in append mode
file.write('This line is appended to the file.\n')  # write a line to the file
file.close()  # close the file

# using with statement to open file
with open('example.json', 'r') as file:  # open the file in read mode
    content = file.read()  # read the entire content of the file
    print(content)  # print the content of the file
    
# we are open with the 'with' keyword as we do not need to close the file by manualy as it will automatically close the file after the block of code is executed
