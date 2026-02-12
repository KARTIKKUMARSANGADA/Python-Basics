# private attributes and methods

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. I live in {self.city}, {self.country}."
    
    
p1 = Person("raj", 30, "surat", "india")


print(p1.greet())
p1.display_info()