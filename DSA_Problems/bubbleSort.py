def bubbleSort(mylist):

    for i in range(len(mylist)):

        for j in range(0,len(mylist)-i-1):
            if mylist[j]>mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp

    return mylist

mylist= [-2, 45, 0, 11, -9, 2, 15]
res=bubbleSort(mylist)
print(res)