class EmobilisStudent:
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and I am {self.age} years old")
#creating an object
myobj=EmobilisStudent("Manvin",19)

myobj.hello_me()

class CarModel:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def blue_blue(self):
        print(f"This is a {self.name} and it is {self.price} only")
myobj=CarModel("Pagani",100000)

myobj.blue_blue()

#
class Magari:
    def __init__(self, model, make, year, properties):
        self.model=model
        self.make=make
        self.year=year
        self.properties=properties
    def white_white(self):
        print(f"This is a {self.model} {self.make} in the year {self.year} and is {self.properties}")
myobj=Magari("Subaru","Legacy",1998,"blue")

myobj.white_white()

#assignment
class Mavazi:
    def __init__(self, designer, type, cost, properties, age):
        self.designer=designer
        self.type=type
        self.cost=cost
        self.properties=properties
        self.age=age
    def clothes_clothes(self):
        print(f"Hello there!This is {self.designer}.We have {self.type} which cost {self.cost} especially in the color {self.properties} and in the age {self.age}. Kindly enjoy your shopping!")
myobj=Mavazi("Versace","tops",1500,"blue",19)
myobj.clothes_clothes()

class Phone:
    def __init__(self, company, model, cost, release):
        self.company=company
        self.model=model
        self.cost=cost
        self.release=release
    def bzz_bzz(self):
        print(f"Hello and welcome to {self.company}.This is the {self.model} which costs {self.cost} which was released in {self.release}")
myobj=Phone("Samsung","S22Ultra",1500,"2022")
myobj.bzz_bzz()


