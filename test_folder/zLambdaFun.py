cube_of=lambda x:x*x*x
res=cube_of(5)
print(res)

add_fn=lambda x,y:x+y
res1=add_fn(7,9)
print(res1)


a=(lambda x:x*x)(9)
print(a)

b=(lambda x,y:x+y)(25,29)
print(b)

c=(lambda x:x*5)(10)
print(c)

num_list=[1,2,3,4,5,6,6]
d=list(filter(lambda x:x>3,num_list))
print(d)

r=list(filter(lambda x:x>2 and x<7, num_list))
print(r)

s=set(filter(lambda x:x>3 ,num_list))
print(s)