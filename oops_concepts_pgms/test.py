class Student:
    clg='ABC'

s=Student()
s.clg='XYZ'
print(s.clg)

print("*************************************************************")

class Car:
    wheels=4
    def __init__(self):
        self.company='BMW'
        self.mil=15

c=Car()
print(c.wheels,c.company,c.mil)

print("*************************************************************")

class CarType:
    wheels=4
    def __init__(self,color,milage):
        self.color=color
        self.milage=milage
        self.comp='BMW'

c1=CarType('white',10)
print(c1)
print(type(c1))
print(c1.comp,c1.wheels)

print("#######################################################################")
class Person:
    str='Hello'

p=Person()
print(p.str)

print("#######################################################################")
class Person1:
    def details(self):
        print("He is a Human!!!")

p1=Person1()
p1.details()