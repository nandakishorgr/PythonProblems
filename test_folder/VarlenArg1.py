def student(*marks,name,school):
    print(name)
    print(school)
    print(marks)
    print(type(marks))
    for i in marks:
        print(i)

student(95,90,85,90,50,65,70,"Yes",'NO','Kishor',1994,name="John",school="Oxford")


def print_fun(*args):
    print(args)
    print(type(args))

print_fun('abc')

def print_fun1(**data):
    print(data)
    print(type(data))
    print(data['company'])
    print(data['age'])
    for i,j in data.items():
        print(i,j)

print_fun1(name='abc',company='Google',age=35)

print("********************************************************************")
def student_college_details(*students,**college):
    print(students)
    print(type(students))
    print("****** Printing all students**********")
    for i in students:
        print(i)

    print("****** Printing College details**********")
    print(college)
    print(type(college))
    for i,j in college.items():
        print(i,":",j)

student_college_details("John","Mike","George","Lilly","Warner","Mary",College_name='STANSFORD',city='NewYork',year='2022',University='oxford')