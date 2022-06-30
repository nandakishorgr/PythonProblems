def mergeSort(my_list):
    if len(my_list)>1:
        mid=len(my_list)//2
        left_list=my_list[:mid]
        right_list=my_list[mid:]

        mergeSort(left_list)
        mergeSort(right_list)

        i=j=k=0

        while(i<len(left_list) and j<len(right_list)):
            #print("HIII")
            #print(left_list,right_list)
            if left_list[i]<right_list[j]:
                my_list[k]=left_list[i]
                i+=1
            else:
                my_list[k]=right_list[j]
                j+=1
            k+=1

        while(i<len(left_list)):
            my_list[k]=left_list[i]
            i+=1
            k+=1
        while(j<len(right_list)):
            my_list[k]=right_list[j]
            j+=1
            k+=1
        #print(my_list)


l=[20,1,50,40,2]
l1=[20,1,50,40,2,7,15,80]
mergeSort(l)
print(l)