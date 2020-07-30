#implementation of queue

#functions
def addition(que,data):
    que.append(data)
    return que

def pop(que):
    if isempty(que):
        return "underflow"
    else:
        que.pop()
        if len(que)==1:
            front=rear=0
        else:
            front=0
            rear= len(que)-1  
        return que

def isempty(que):
    if len(que)==0:
        return True
    else:
        return False

def peek(que):
    if isempty(que):
        return "underflow"
    else:
        rear=len(que)-1
        return(que[rear])

def show(que):
    if isempty(que):
        return "underflow"
    else:
        rear=len(que)-1
        for i in range (rear, -1, -1):
            print (que[i])
    



#main programme
que=[]
front=rear=[]
while True:
    print ("1. add")
    print ("2. deleted")
    print ("3. peek")
    print ("4. show the entire queue")
    ch= int(input("enter a number from the choices: "))
    if ch==1:
        data= int(input("enter a number to add to the queue: "))
        addition(que, data)
        print ("successfully added")
        print (que)
            
    elif ch==2:
        a=pop(que)
        if a=="underflow":
            print ("underflow!")
        else:
            print ("task done")

    elif ch==3:
        a=peek(que)
        if a=="underflow":
            print ("underflow!")
        else:
            print (a)

    elif ch==4:
        a=show(que)
        if a=="underflow":
            print ("underflow!")
        else:
            pass

    else:
        continue

        

        
