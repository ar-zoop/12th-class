#liner list search
def lsearch(a,lst):
    for i in range (len(lst)-1):
        if lst[i]==a:
            print ("the pos of the element is" ,-i)
        else:
            print("uh oh, element not fuond
                  1")


n=int(input("enter no of elements to add tot the list: "))
lst=[]
for i in range (n):
    b=int(input("enter the no to add to the listy: "))
    lst.append(b)
a= int(input("enter the no to search"))
lsearch(a,lst)
