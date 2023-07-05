def linearsearch(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1
arr=[1,23,4,5,89]
result=linearsearch(arr,n=len(arr),key=5)
if result==-1:
    print("elament not found")
else:
    print("found at  index:",result)
