def add(stk,data):
    a=stk.append(data)
    return a
def pop(stk):
    if is_empty(stk):
        return "underflow"
    else:
        stk.pop()
        top=len(stk)-1
        return top
        
def is_empty(stk):
    if len(stk)==0:
        return True
    else:
        return False


def peek(stk):
    if is_empty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if is_empty(stk):
        print ("empty")
        exit
    else:
        for i in range (len(stk)-1,-1,-1):
            print (stk[i])


stk= []
top= None
while True:
    print ("1. add")
    print ("2. pop")
    print ("3. peek")
    print ("4. show thw whole stck")
    print ("5. exit")
    ch= int(input("enter a number of choice: "))
    if ch==1:
        data= int(input("enter the number to add: "))
        add(stk,data)

    elif ch==2:
        a=pop(stk)
        if a=="underflow":
            print ("underflow")
        else:
            pass

    elif ch==3:
        a=peek(stk)
        if a=="underflow":
            print ("underflow")
        else:
            print (a)

    elif ch==4:
        display(stk)            

    
