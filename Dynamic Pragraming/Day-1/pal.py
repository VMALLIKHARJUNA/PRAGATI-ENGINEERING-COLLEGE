a=list(map(int,input().split()))
s=0
for i in a:
    if i%2==0:
        s=s+i
y=str(s)
r=y[::-1]
if r==y:
    print("yes")
else:
    print("no")