#binary sort

#functions

def binary(a,data):
    start=0
    end= len(a)-1
    while start<=end:
        mid= (start+end)//2
        if a[mid]==data:
            return mid
        elif a[mid]>data:
            end=mid-1
        else:
            start=mid+1

    else:
        return -999



#main programe
a=[12,2,23,3,34,4,45,5,56,67,99,100]
a.sort()
print (a)
data= int(input("enter a number to search: "))
s=binary(a,data)
if s>=0:
    print (s+1)
else:
    print ("not found")
