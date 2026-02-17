# Data attributes can be added anytime
# You can add variables to an object even after it is created.


class Details:
    name = 'kartik'
    age = 22
    City = 'ahmd'

k1 = Details()
print(k1.name)
print(k1.age)
print(k1.City)

k2=Details()
k2.City = 'Surat'
print(k2.City)
print(k1.City)


# 
# 

details = []

class Class:
    def __init__(self):
        self.data = []

    def add(self,name ):
        self.details.append[name]
        self.data.append(name)

    def addtwice(self, name):
        self.add(name)
        self.add(name)