#implemenattion of queue
##functions
def add(stk,data):
    if isfull(stk):
        return "overflow"
    else:
        a=stk.append(data)
        front=len(stk)-1
        rear=0
        return a
def pop(stk):
    if is_empty(stk):
        return "underflow"
    else:
        stk.pop()
        front=len(stk)-1
        return front
        
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
        front= len(stk)-1
        rear=0
        for i in range (len(stk)-1,-1,-1):
            print (stk[i])

def isfull(stk):
    if len(stk)==10:
        return True
    else:
        return False



##mian programme
stk= []
front=rear= None
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
        a=add(stk,data)
        if a=="overflow":
            print ("overflow")
        else:
            print ("succesfully added")

    elif ch==2:
        a=pop(stk)
        if a=="underflow":
            print ("underflow")
        else:
            print ("sucessfully deleted")

    elif ch==3:
        a=peek(stk)
        if a=="underflow":
            print ("underflow")
        else:
            print (a)

    elif ch==4:
        display(stk)

    elif ch==5:
         break
        
    else:
        continue
    








        
