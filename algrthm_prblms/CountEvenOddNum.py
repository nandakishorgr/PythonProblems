s=[2,5,6,10,16,17,23,26,29,30]

def countEvnOdd(s):
    even=0
    odd=0
    even_nums=[]
    odd_nums=[]
    for i in s:
        if i%2==0:
            even_nums.append(i)
            even+=1
        else:
            odd+=1
            odd_nums.append(i)
    print("even numbers are:",even_nums)
    print("odd numbers are:",odd_nums)
    print("even numbers count is:",len(even_nums))
    print("odd numbers count is:",len(odd_nums))
    return even,odd


even,odd = countEvnOdd(s)
print("even nums count is",even)
print("odd nums count is",odd)