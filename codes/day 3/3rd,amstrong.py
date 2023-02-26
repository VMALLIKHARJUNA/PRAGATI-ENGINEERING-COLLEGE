'''
i=int(input("enter a number:"))
s=0
n=i
while (n!=0):
    r=n%10
    #print("r=",r)
    s=s+(r**3)
    #print("s=",s)
    n=n//10
    #print("n=",n)
if(s==i):
    print("given number is amstrong")
else:
    print("given number is not an amstrong number ")
'''
    
#universal
x=1
while(x>0):
    
    i=int(input("enter a number:"))
    p=len(str(i))
    s=0
    n=i
    while (n!=0):
    
        r=n%10
        #print("r=",r)
        s=s+(r**p)
        #print("s=",s)
        n=n//10
        #print("n=",n)
    if(s==i):
        print("given number is amstrong")
    else:
        print("given number is not an amstrong number ")

    
