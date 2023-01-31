t=21
l=int(input("enter no of lemons you have:"))
if  t < l:
    s=l-t
    print("you have ",s,"more lemons")
elif t==l:
    print("you have 21 lemons")
elif 0 <  l < t:
    s=t-l
    print("you have",s,"less lemons")
elif l < 0:
    print("please enter valid number")
    
