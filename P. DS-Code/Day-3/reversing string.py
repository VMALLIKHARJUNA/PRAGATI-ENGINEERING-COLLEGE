x=input()
y=list(x)
z=[]
d=len(y)-1
for i in range(len(y)):
    if 96< ord(y[i])<123 or 64< ord(y[i])<91:
        for j in range(d,-1,-1):
            if 96< ord(y[j])<123 or 64< ord(y[j])<91:
                z.insert(i,y[j])
                print(z)
                break
            else:
                d=d-1
        d=d-1
    else:
        print(y[i])
        z.insert(i,y[i])
        print(z)                
print(*z,sep="")
