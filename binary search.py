##binary search

#functions
def binary(a,data):
    start=0
    end= len(a)-1
    while start<=end:
        mid= int((start+end)/2)
        if data==a[mid]:
            return mid
        elif a[mid]>data:
            end=mid-1
        else:
            start=mid+1

    else:
        return -999

    
#main programme
a=[12,2,23,3,34,4,45,5,56,67,99,100]
a.sort()
print (a)
data= int(input("enter a number to search: "))
s=binary(a,data)
if s>=0:
    print (s)
else:
    print ("not found")
