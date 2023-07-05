def fib(n):
    f1=0
    f2=1
    l=[0,1]
    for i in range(2,n):
        f3=f1+f2
        l.append(f3)
        f1=f2
        f2=f3
    return l[-1]
n=int(input())
print(fib(n))
#---------------------------------
def fib(n):
    if n<0:
        print("Invalid input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(7))

