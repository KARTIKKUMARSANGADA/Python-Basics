for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # end used for the end of the line and it is used to print the next line in the same line
    
    print(repr(x*x*x).rjust(4))
# it will print the value of x, x*x and x*x*x in a formatted way with 2, 3 and 4 spaces respectively
# rjust() is used to right justify the string and it takes the width of the string as an argument and it will add spaces to the left of the string to make it right justified

print('12'.zfill(5))
# it will add zeros to the left of the string to make it 5 characters long

print('-20'.zfill(7))
# it will add zeros to the left of the string to make it 5 characters long and it will keep the negative sign at the beginning of the string

print('3.14159265359'.zfill(20))
# it will add zeros to the left of the string to make it 10 characters long and it will keep the decimal point at the correct position

