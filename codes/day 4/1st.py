'''text="india"
index=0
for i in text:
    print("text [", index,"]=",i)
    index+=1


import string
print(string.digits)
print(string.ascii_letters)

x=1
while(x==1):
    
    t=int(input("enter value:"))
    for i in range(1,t+1):
        if(i%2==0):
                print('{}th term is {}'.format(i,(i//2)-1))
        else:
                print('{}th term is {}'.format(i,(i-1)))
'''             

str1="listen"
str2="silent"
a=len(str1)
b=len(str2)
if(a==b):
    sortstr1=sorted(str2)
    sortstr2=sorted(str1)
    if sortstr1==sortstr2:
        print("anagram")
    else:
        print("it is not an anagram")
else:
    print("not equal")
    









































