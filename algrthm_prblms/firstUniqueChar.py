#Given a string, find the first non-repeating character in it and return it’s index. If it doesn’t exist, return -1.

s= "eetcode"
def first_uniq_char(s):
    dup = {}
    for i in s:
        dup[i] = dup.get(i,0) + 1
        #dup[i]=1
        print(dup)
    print(dup)
    for i in range(len(s)):
        if dup[s[i]] == 1:
            return i
    return -1
res=first_uniq_char(s)
print("first Uniue Char index value is :",res)
