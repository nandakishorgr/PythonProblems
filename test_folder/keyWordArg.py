def student(name,maths,phy,chem):
    print("Student name:",name)
    print("Phy:",phy,"chem:",chem,"maths:",maths)
    return maths+phy+chem
"""
s2=student(name='John',maths=85,phy=75,chem=80)
print(s2)

s3=student(name='Alex',maths=85,phy=90,chem=80)
print(s3)

s4=student('Lilly',95,phy=90,chem=90)
print(s4)

s5=student('Kishor',95,95,95)
print(s5)

s6=student(name='Nanda',maths=90,phy=96,chem=94)
print(s6)

s7=student(chem=94,name='XYZ',phy=99,maths=100)
print(s7)
"""

def employee(name,age,sal,country='India'):
    print("name",name)
    print("age",age)
    print("salary",sal)
    print("country",country)

#employee(sal=9000,name='JOHN',age=28)


def employee1(name,age,sal,occupn='Engineer',country='India'):
    print("name",name)
    print("age",age)
    print("salary",sal)
    print("country",country)
    print("occpn:",occupn)


employee1(name='Kishor',age=40,sal=8000)
