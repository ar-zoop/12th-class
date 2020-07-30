#function
def binary (a,data):
    start=0
    end=len(a)-1
    while start<=end:
        mid= (start+end)//2
        if data==a[mid]:
            return mid
        elif data>a[mid]:
            start=mid+1
        else:
            end= mid-1
    else:
        return -999

#main programme
a=[12,2,23,3,34,4,45,5,56,67,99,100]
a.sort()
data=int(input("enter a number to search in the list: "))
s=binary(a,data)
if s>-1:    
    print (s+1)
else:
    print (":not herre")
