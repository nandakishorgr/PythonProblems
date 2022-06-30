fruits={}

fruits['Banana']=10
fruits['Mango']=20
fruits['Apple']=30
fruits['Orange']=40
fruits['Grapes']=[20,40,60]


fruits['Banana']+=100
fruits['Mango']=fruits['Mango']+200
print(fruits)


for i,j in fruits.items():
    print(i,j)
print("****************************************************************")
a=set()
print(a)
print(type(a))

b=set([1,2,3,3,4])
print(b)
print(type(b))

str='radar'
c=set(str)
print(c)

d=set([5,6,6,7,8])
print(d)

q=set("kishor")
q.add('z')
q.remove('k')
print(q)