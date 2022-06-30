print("***************Working with LISTS *************************************************")

some_list=[1,2,3,4,5]

some_list[2]=60
print(some_list)

for i in range(len(some_list)):
    some_list[i]=some_list[i]*10
print(some_list)


print("***************Working with DICTS *************************************************")

fruit_qty={}
fruit_qty['Banana']=10
fruit_qty['Mango']=20
fruit_qty['Orange']=30
fruit_qty['Apple']=50

print(fruit_qty)

fruit_qty['Banana']=fruit_qty['Banana']+90

print(fruit_qty)

print("*******************************************************************************")

val_dict={'a':10,'b':20,'c':30,'d':40}
print(val_dict)
print(val_dict.get('z',999))


for i in val_dict:
    val_dict[i]=val_dict[i]*10
print(val_dict)

cars={'name':'BMW','year':2022,'country':'India'}
print(cars.get('country'))
print(cars.get('price'))
print(cars.get('price',50000))

print("****** for loop opern *****")
for i in cars:
    print(i)