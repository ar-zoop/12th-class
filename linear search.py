#functions
def line(lst,data):
    for i in range (0,len(lst)):
        if lst[i]==data:
            return i
        else:
            return -999
            

#main pprogramme
a=[12,2,23,3,34,4,45,5,56,67,99]
data= int(input("enter a number to srerach: "))
a=line(a,data)
if a>=0:
    print (a, "is the position of the element found")
else:
    print ("element not found")
    
    
