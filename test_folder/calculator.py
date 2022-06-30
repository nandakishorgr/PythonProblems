def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def Calculator(a,b,opertr):
    if opertr=='add':
        return add(a,b)
    if opertr=='sub':
        return sub(a,b)
    if opertr=='mul':
        return mul(a,b)
    if opertr=='div':
        return div(a,b)


res=Calculator(10,5,'add')
print(res)

res1=Calculator(10,5,'sub')
print(res1)

res2=Calculator(10,5,'mul')
print(res2)

res3=Calculator(10,5,'div')
print(res3)

res4=Calculator(10,15,"abc")
print(res4)