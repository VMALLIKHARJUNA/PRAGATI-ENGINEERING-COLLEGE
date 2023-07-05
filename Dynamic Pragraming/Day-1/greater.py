l=list(map(int,input().split()))
g=l[0]
for i in l:
    if g<i:
        g=i
print(g)