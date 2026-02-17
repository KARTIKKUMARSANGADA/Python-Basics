

class MyClass:
    
    def __init__(self):
        pass
    
    i = 12345

    def f(self):
        return 'hello python'
    
x = MyClass() # created an object of class as x
print(MyClass.f)
print(x.i)      
print(x.f())



class Complex:
    def __init__(self, name, age):
        self.n = name
        self.a = age

x = Complex('kartik',20)
print(x.n)
print(x.a)
