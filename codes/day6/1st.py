def square(y,z):
    return y**2+z**2
n=int(input("Enter a number:"))
x=n
s=0
u=0
while(n!=0):
    r=n%10
    n=n//10
    s=s+square(r,n)
while(s!=0):
    p=s%10
    s=s//10
    u=u+square(p,s)
if(u==1):
    print("Yes")
else:
    print("No")
