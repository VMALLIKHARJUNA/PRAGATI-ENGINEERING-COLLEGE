l=list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
for k in range(len(l)):
    print(l[k])

