l=list(map(int,input().split(",")))
def f(a):
    r=[]
    for i in range (len(a)):
        if a[i]==max(a):
            a.pop(i)
            a.insert(i,0)
        else:
            b=a[i]
            r.append(i)
            break
    for j in range(len(a)):
        if a[j]==max(a):
            s=a[j]
            r.append(j)
            break
    p=s-b
    r.append(p)
    return r
print(f(l))
