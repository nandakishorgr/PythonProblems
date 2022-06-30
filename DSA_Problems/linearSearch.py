def linerSearch(my_list,x):
    for i in range(len(my_list)):
        if my_list[i]==x:
            return i
    return -1


mylist=[2,4,0,1,9,3,8,15,45,33]
x=15
res=linerSearch(mylist,x)
print("position of the ele is:",res)
