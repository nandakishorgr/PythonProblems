cube=lambda x:x*x*x
res=cube(5)
print(res)


add=lambda x,y:x+y
res1=add(10,20)
print(res1)

mul=lambda x,y,z:x*y*z
res3=mul(2,6,5)
print(res3)

a=(lambda x:x*x)(9)
print(a)

b=(lambda x,y: x+y)(7,8)
print(b)

c=(lambda x:x+10)(70)
print(c)

tot_marks=lambda phy,chem,maths,bio=100:phy+chem+maths+bio
ress=tot_marks(10,20,50)
print("final result is",ress)

num_list=[1,2,3,4,5,6,7,8]
print("************** printing ********************************************")
qq=filter(lambda x:(x%2==0),num_list)
print(qq)
print(list(qq))

print("************** printing ********************************************")
zz=lambda x:x>5
print(zz)
pp=filter(zz,num_list)
print(list(pp))

y=(lambda x:x+30)(10)
print(y)