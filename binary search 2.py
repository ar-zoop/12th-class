#binary search
def bsearch(lst,data):
     length=len(lst)-1
     mid=len(lst)//2
     while mid>=0 and mid<=length:
         if  data==lst[mid]:
             return ("element found at", mid+1,"position")
             
         elif data>lst[mid]:
             mid=mid+1
         else:
            mid=mid-1

     print("uh oh not found")


n=int(input("enter number of elements you want in thelist: "))
lst=[]
for i in range (n):
    a=int (input ("enter the element you wanna input: "))
    lst.append(a)
ele=int(input("enter the number you wAnna search: "))
bsearch(lst,ele)
