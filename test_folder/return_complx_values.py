def find_max_elem(some_list):
    if len(some_list)==0:
        print("its an empty list!!")
        return None
    max_ele=some_list[0]
    for i in range(1,len(some_list)):
        if some_list[i] > max_ele:
            max_ele=some_list[i]
    return max_ele

a_list=[15,22,83,48,65]
b_list=[]

res=find_max_elem(a_list)
print("Max ele is:",res)


def ret_dict(name,age,occup):
    dict_sample={"name":name,"age":age,"occup":occup}
    return dict_sample

res1=ret_dict("kishor",30,"manager")
print(res1)
print(type(res1))


def gen_list(name,num_times):
    l=[]
    for i in range(num_times):
        l.append(name)
    return l

res2=gen_list("kishor",4)
print(res2)
print(type(res2))

def pos_neg(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "ZERO"
q=pos_neg(0)
print(q)