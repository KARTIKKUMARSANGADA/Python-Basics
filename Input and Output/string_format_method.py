# Basic usage of the str.format() method 


print(f'my name is {0} and my age is {1}'.format('kartik', 22))

# it will replace the first {} with 'kartik' and the second {} with 22


table = {'kartik': 123, 'parth': 234, 'ravi': 345}
print('kartik: {0[kartik]:d}; ravi: {0[ravi]:d}; '
      'parth: {0[parth]:d}'.format(table))
# it will replace the first {} with the value of 'kartik' in the table, the second {} with the value of 'ravi' in the table and the third {} with the value of 'parth' in the table


table = {'kartik': 123, 'parth': 234, 'ravi': 345}
print('kartik: {kartik:d}; parth: {parth:d}; ravi: {ravi:d}'.format(**table))
# it will replace the first {} with the value of 'kartik' in the table, the second {} with the value of 'parth' in the table and the third {} with the value of 'ravi' in the table **table is used to unpack the table and pass the values as keyword arguments to the format() method


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
# it will print the value of x, x*x and x*x*x in a formatted way with 2, 3 and 4 spaces respectively
# {index:width type} is the syntax for formatting the output using the format() method


