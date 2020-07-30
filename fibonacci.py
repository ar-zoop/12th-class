#fibonacci series

def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return (fib(x-1)+fib(x-2))

x=int(input("enter a range for fibanacci series: "))
for i in range (0,x):
    print (fib(i), ",", end="")
    
