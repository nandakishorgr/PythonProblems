def checkAnagrm(str1,str2):
    if set(str1.lower()) == set(str2.lower()):
        print("Strings are anagrams")
    else:
        print("Strings are NOT anagrams")

checkAnagrm('listen', 'silent')

def checkAnagrm1(str1,str2):
    if len(str1)==len(str2):
        s1=sorted(str1)
        s2=sorted(str2)
        if (s1==s2):
            print("They are Anagrams")
        else:
            print("They are not Anagrams")
    else:
        print("Strings lengths are not equal!!!")

checkAnagrm1('listen', 'silent')