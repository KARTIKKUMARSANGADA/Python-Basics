# 4.9.1

# default argument 
def greet(name="Guest"):
    print("Hello", name)

greet("Amit")
greet()

# bydefault there is one value assigned to name parameter i.e. "Guest", so when we call greet() without any argument, it will print "Hello Guest". But when we call greet("Amit"), it will override the default value and print "Hello Amit".


# Keyword argument
def greet(name, message):
    print(message, name)
    
greet(name="Amit", message="Welcome")
#in this example you have to specify the parameter names when calling the function, so that the arguments can be passed in any order. In this case, we are passing the name parameter as "Amit" and the message parameter as "Welcome". The output will be "Welcome Amit".

# 4.9.3

# positional or keyword arguments

def add(a, b):
    print(a + b)

add(2, 3)
add(a=2, b=3)


# positional arguments
def add(a, b, /):
    print(a + b)

add(2, 3)

# in this case, the arguments are passed in the same order as the parameters defined in the function. before the / symbol indicates that a and b are positional-only parameters

# keyword arguments
def add(*, a, b):
    print(a + b)

add(a=2, b=3)
# in this case, the arguments are passed with the parameter names, so the order of the arguments does not matter. You can also call add(b=3, a=2) and it will still work correctly.after the * symbol indicates that a and b are keyword-only parameters

# example function combined
def func(a, b, /, c, *, d):
    print(a, b, c, d)

func(1, 2, 3, d=4)

# here, a and b are positional-only parameters.
# c is a regular parameter.
# d is a keyword-only parameter.

# 4.9.4

def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4)
# * taking multiple  arguments and packing them into a tuple called numbers. 

def total(**numbers):
    print(numbers)
total(a=1, b=2, c=3)
# ** taking multiple keyword arguments and packing them into a dictionary called kwargs. In this case, the output will be {'a': 1, 'b': 2, 'c': 3}.


# 4.9.5

def add(a,b,c):
    print(a + b + c)
list=[1, 2, 3]
add(*list)
# * is used for list and tuple unpacking. 
# here we are passing three arguments to the add function, which will print the sum of those arguments. The * operator is used to unpack the list and pass its elements as separate arguments to the function.


def add(a, b, c):
    print(a + b + c)
dict = {'a': 1, 'b': 2, 'c': 3}
add(**dict) 
# ** is used for dictionary unpacking.
# here we are passing three keyword arguments to the add function, which will print the sum of those. The ** operator is used to unpack the dictionary and pass its key-value pairs as keyword arguments to the function.


# 4.9.6 
a = lambda x, y: x + y
print(a(2, 3))
# makinng in a single line, the lambda function takes two arguments x and y and returns their sum. When we call a(2, 3), it will return 5.

# 4.9.7

def documented_function():
    """This is a documented function."""
    pass
print(documented_function.__doc__)
# here it print the docstring of the function.

# 4.9.8

def add(a: int, b: int) -> int:
    return a + b
print(add.__annotations__)
# just for information no any rules.
# here we are using type hints to indicate that the add function takes two integer arguments and returns an integer.