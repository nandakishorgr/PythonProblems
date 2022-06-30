class Student:
    clg='ABC Institue'

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.branch='ECE'
        self.result=9.5

    def displayDetails(self):
        print(self.name,self.age,self.branch)
        print(self.clg)
        print(Student.clg)

    def totMarks(self):
        print(self.result)


s1=Student("John",20)
s1.displayDetails()

s2=Student("Mary",25)
s2.displayDetails()





