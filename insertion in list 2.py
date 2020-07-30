#insertion in a list
#incomplete
def insert(lst, data):
    a=lessthanzero(lst,data)
    if a==0:
        lst.append(None)
        for i in range(len(lst)):
            while u<
    else:
        u=len(lst)-1
        v=len(lst)
        lst.append(None)
        for i in range(v):
            if data<lst[u]:
                #shifting
                lst[u+1]=lst[u]
                u=u-1
            else:
                lst[u+1]=data
                print ("done at pos", u)
                print(lst)
                break

def lessthanzero(lst,data):
    length=len(lst)
    for i in range (length):
        if data<lst[0]:
            return 0
        else:
            return -1
        


n=int(input("enter number of elements you want in thelist: "))
lst=[]
for i in range (n):
    a=int (input ("enter the element you wanna input: "))
    lst.append(a)
lst.sort()
ele=int(input("enter the number you wAnna insert: "))
insert(lst,ele)
