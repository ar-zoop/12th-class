##stack implementation

#functions
def insert(stk,data):
    stk.append(data)
    top=len(stk)-1

def pop(stk):
    if isempty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top = None            
        else:
            top= len(stk)-1
        return item

def isempty(stk):
    if len(stk)==0:
        return True
    else:
        return False

def peak(stk):
    if isempty(stk):
        return "underflow"
    else:
        top= len(stk)-1
        return(stk[top])

def show(stk):
    if isempty(stk):
        print( "underflow")
    else:
        top=len(stk)-1
        for i in range (top,-1,-1):
            print (stk[i])

#main programme

stk= []
top= None
while True:
    print ("1. add")
    print ("2. delete")
    print ("3. peek")
    print ("4. show entire stack")
    print ("5. exit")
    ch= int(input("enter a number of choice: "))
    if ch==1:
        data= int(input("type the number to insert: "))
        insert(stk,data)
        print ("addition successful")

    elif ch==2:
        a=pop(stk)
        if a== "underflow":
            print ("underflow!")
        else:
            print ("deleted successfully")

    elif ch==3:
        a=peak(stk)
        if a=="underflow":
            print ("underflow")
        else:
            print (a)

    elif ch==4:
        a=show(stk)
        
    elif ch==5:
        break

    else:
        continue
        

    
