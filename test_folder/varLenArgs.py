def person(name,*data):
    print(data)
    print(name)
    print(type(data))
    for i in data:
        print(i)

person("ABC",28,"india",10000)

def sum(*values):
    res=0
    for i in values:
        res=res+i
    print("Sum is :",res)

sum(10,20,30,40,50,30)

print("*********************************************************")
def employee(name,**data):
    print(data)
    print(type(data))
    for i,j in data.items():
        print(i,j)

employee("XYZ",age=30,country="india",sal=10000,city="Blore")