def find_max_in_list(num_list):
    max_ele=num_list[0]
    min_val=num_list[0]
    for i in range(1,len(num_list)):
        if num_list[i]>max_ele:
            max_ele=num_list[i]
        if num_list[i]<min_val:
            min_val=num_list[i]
    return max_ele,min_val

num_list=[10,250,150,9,45,22,12]

max_num,min_num=find_max_in_list(num_list)
print("Max number in a list is :",max_num)
print("Min number in a list is :",min_num)