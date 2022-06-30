def add():
    print("Result of add fun is:::$$")

def sub():
    print("Result of Sub fun is")

def main():
    print("inside main fun of calc module",__name__)
    add()
    sub()
#main()
if __name__=='__main__' :
    main()
