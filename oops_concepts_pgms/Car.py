class Car:
    wheels=4

    def __init__(self,owner):
        self.color='White'
        self.comp='BMW'
        self.price='1000'
        self.owner=owner
        self.dict={}

    def print_details(self):
        self.dict={'name':self.owner,'comp':self.comp,'color':self.color}
        print(self.dict)

    def change_details(self):
        self.dict={'name':'PQR','age':30}
        print(self.dict)
        print(self.wheels)


c1=Car("Kishor")
c1.print_details()

c2=Car("ABCD")
c2.print_details()