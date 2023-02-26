'''
cubes=[]
for i in range(11):
    cubes.append(i**3)
print(cubes)
'''
num=[int(d) for d in str(input("enter number:"))]
even,odd=0,0
print(num)
for i in range (0,len(num)):
    if i%2==0:
        even=even+num[i]
    else:
        odd=odd+num[i]
print(abs(odd-even))
