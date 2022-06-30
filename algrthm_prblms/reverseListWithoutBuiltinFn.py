def reverse_fn(sl):
    rev_list=[]
    for i in range(len(sl)):
        rev_list.append(sl[len(sl)-1-i])
    print(rev_list)


def reverse1(sl):
    new_list=sl[::-1]
    return new_list


int_list=[12,9,32,45,77,82,94]
reverse_fn(int_list)

res=reverse1("Nandakishor")
print(res)



