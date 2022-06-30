def findDups(l):
    dict={}
    for i in l:
        print(dict)
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    for i,j in dict.items():
        if j>1:
            print(i)

#findDups([2, 10,10, 100, 2, 10, 11,2,11,2])


#Time Complexity: O(N)
#Auxiliary Space: O(N)
