lst=[]
while True:
    enter=input("enter a number: ")
    if enter =="done" or enter =="Done":
        break
    else:
        try:
            c_enter =float(enter)
        except:
            print ("not correct boss")
            continue
   
   
        lst.append(c_enter)

count=summ=0

for i in lst:
    count=count+1
    summ=summ+i

print ("count is " , count)
print("sum is ",summ)
print("avg is ", summ/count)
