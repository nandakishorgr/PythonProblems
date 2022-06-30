import copy

'''
num=[1,2,3,4]
new_num=num
print(num)
print(new_num)

new_num[1]=9
print(id(num))
print(id(new_num))
'''

num=[[1,2,3],[4,5,6],[7,8,9]]
new_num=copy.copy(num)

print(num)
print(new_num)

new_num[0][0]=1000

print(num)
print(new_num)

new_num[0]="something else"
print(new_num)
print(num)