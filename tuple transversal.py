t1=tuple(input("enter"))
n=input("enter what u wanna find: ")
count=0
for i in t1:
    if i!=n:
        count=count+1
    else:
        break
print(count)
