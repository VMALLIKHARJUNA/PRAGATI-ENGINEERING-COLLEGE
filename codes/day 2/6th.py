'''for i in range(1,151):
    if(i%10==0):
        print(i,end=" ")

for i in range(1,30,2):
    print(i*5,end=" ")
for i in range(-10,0):
    print(i,end=" ")

for i in range(97,123):
    for j in range(97,i+1,2):
        if(i%2!=0):
            print(chr(i),end=" ")
    print("\n")

for i in range(1,11):
    print(i,"*10=",i*10)
'''
i=1

while(i<=6):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print("\n")
    i=i+1   

