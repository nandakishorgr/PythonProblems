def check_num(num):
    if num:
        print("executing if block as: This is non-zero number -->",num)
    else:
        print("executing else block as: This is a zero number -->",num)

check_num(0)
check_num(5)

l1=[]
l2=['a','b','c','d']

def check_list(list):
    if list:
        print(list)
    else:
        print("Its empty List!!!")

check_list(l1)
check_list(l2)