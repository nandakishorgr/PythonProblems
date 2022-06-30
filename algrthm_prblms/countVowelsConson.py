def countVowelsConsonents(str):
    str=str.lower()
    vow_count=0
    cons_count=0

    for i in str:
        if i in ('a','e','i','o','u'):
            vow_count+=1
        else:
            cons_count+=1
    return vow_count,cons_count

v_res,c_res=countVowelsConsonents("ABCDE")
print("Vowels count",v_res)
print("Consonents count",c_res)