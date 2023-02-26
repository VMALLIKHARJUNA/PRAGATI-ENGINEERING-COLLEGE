'''
num=[1,2,3,4,5,6,7,8,9,10]
print(num)
print("first ele in list",num[0])
print(num[2:5])
print(num[::2])
print(num[1::3])
del num[2:4]
print(num)

num=[1,'a',"abc",[2,3,4],5.6]
print(num)

n=int(input("enter n value:"))
s=0
i=1
while(i<=n):
    s=s+i
    i=i+1
print(s)

num=[1,2,3,4,15,6,7,8,9,10]
print(sorted(num))
'''
num=[12,-2,-33,84,-2]
num.append(0)
print(num)
print(num.count(-2))
num.insert(3,100)
print(num)
num.remove(12)
print(num)
num.reverse()
print(num)

num=str(input("enter value:"))
print(int(num,17))

















