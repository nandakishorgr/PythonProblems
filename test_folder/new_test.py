interval=[[1,2],[5,6],[4,7]]
print(interval)
print(type(interval))
l=[1,5,3,4]
l.sort()
print(l)

interval.sort()
print(interval)

l2=[[2,6]]

print(l2[0])

print("***********************************************************")
lst=[]

if not lst:
    print("empty list!!")
else:
    print("Valid list")
print("***********************************************************")

nums=[5,9,3,7,2,8]
for i,n in enumerate(nums):
    print(i,n)
print("***********************************************************")
runs={}
runs['Sachin']=100
runs['Dravid']=90
runs['Ganguly']=60
runs['Sehvag']=50

print(runs)
print(runs['Dravid'])

reg={}
reg[1]=100
reg[2]=50
reg[5]=80

print(reg)
print(reg[2])