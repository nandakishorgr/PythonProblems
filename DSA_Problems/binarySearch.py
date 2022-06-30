def binarySearch(some_list,x):
    left=0
    right=len(some_list)-1

    while left<=right:
        mid=left+(right-left)//2

        if some_list[mid]==x:
            return mid
        elif some_list[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1

some_list=[1,2,4,6,8,9]
x=8
some_list1=[3,4,6,7,8,9,12,15,24,32,44,66,82]
x1=7
result=binarySearch(some_list1,x1)
if result!=-1:
    print("elemnt found in the index pos:",result)
else:
    print("element not found!!")
