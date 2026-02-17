class Dog:
    kind = "canine"   # class variable

d1 = Dog()
d2 = Dog()

print(d1.kind)
print(d2.kind)
# both pbject use the same variable

class Dog:
    kind ="cutie"   # class variable
    
    def __init__(self,name):
        self.name = name  #instance variable
    
    def __repr__(self):
        return f'my dog name is  {self.name} and kind is {self.kind}'  #it used to print all variables or all details
    
        
        
# dog=Dog('shephard')
# print(dog.name)
# print(dog.kind)

dog1=Dog('parth')

print(dog1)
print(dog1.name)
print(dog1.kind)     

# print(dog.name,dog1.kind)       