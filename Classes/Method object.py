# A method object is a function that belongs to an instance of a class.
# When you call a method using an object, Python automatically sends the object as self.


class MyClass:
    def greet(self):
        print("Hello!")

x = MyClass()  
x.greet()
# here greet is method object
