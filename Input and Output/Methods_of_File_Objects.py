# here we are printig the whole file 
with open('example.txt', 'r') as file:
    content = file.read()  # read the entire content of the file
    # print(content)  # print the content of the file
    # now we will read the file line by line
    for line in file:
        print(line)  # print each line of the file
    
    
    
# If you want to read all the lines of a file in a list you can also use list(file) or f.readlines(files).
with open('example.txt', 'r') as file:
    print(list(file))  # read all the lines of the file and return a list of lines
    # print(file.readlines())  # read all the lines of the file and return a list of lines
    # print(file.readline())
    # print(file.readline())
    
# work with binary files r for reading, w for writing,b for binary, + for updating (reading and writing)
with open('workfile', 'wb+') as f:
    f.write(b'0123456789abcdef')  # write a binary string to the file

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file

f.read(1)

f.seek(-3, 2)  # Go to the 3rd byte before the end

f.read(1)

# after we go to any element and then if we print it start from that element no the initial element of the file


