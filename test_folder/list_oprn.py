num_list=[1,2,3,4,5,6]

cars_list=['Tata','Honda','Nissan','BMW','Ford']

num_list+=[7,8]
num_list.extend([9,10])
print(num_list)
print(type(num_list))

print(num_list[0:4])

print(num_list[:])
print(num_list[0:5])
print(num_list[2:5])
print(num_list[0:5:2])


print(num_list[::-1])
print(num_list[5:0:-1])

print(cars_list[0:4])

print(cars_list[2:4])
print(cars_list[:3])
print(cars_list[2:])

a="9ACT56YRS"
print(a[0])
print(a[4:7])
print(a[4:5] + a[6:7])

x,y,z,q,w='NANDA'
print(x,y,z)

cars_list[2]='AUDI'
print(cars_list)
cars_list+=['AUDI']
print(cars_list)

print("******************* SPlit & JOIN ****************************************************")
city = "Hello New York City"

a=city.split()
print(a)
print(type(a))

b= ",".join(a)
print(b)
print(type(b))

c="|".join(a)
print(c)

print(city[::-1])

new_list=['Tata','Honda','Nissan','BMW','Ford']
z=new_list[::-1]
print(z)
print(type(z))
q=len(new_list)
print(q)

