def countChar(str,char):
    count=0
    for i in str:
        if i==char:
            count+=1
    print("No of occurences of the Char:",char,"is:",count)

countChar("programmer",'m')