def findUniqCharInd(ss):
    dict={}
    for i in ss:
        dict[i]=dict.get(i,0)+1
    print(dict)

    for i,j in dict.items():
        if j>1:
            print(i,j)

    for i in range(len(ss)):
        if dict[ss[i]]==1:
            return i

res=findUniqCharInd("eetcode")
print("The index posn of unique char is:",res)