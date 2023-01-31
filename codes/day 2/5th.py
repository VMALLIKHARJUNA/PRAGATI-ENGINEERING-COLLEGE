E=84
S=100
D=2.00
C=3000
e=int(input("enter day:"))
if(e<E):
    
    c=int(input("enter no of calls: "))
    s=int(input("enter no of sms:"))
    d=float(input("enter data used:"))
    if(e<E and s<S and c<C  and d<D ):
        print("plan expires with in",E-e,"days")
        print("till you have ",C-c,"calls")
        print("till",S-s,"sms left")
        print("till you have",D-d,"data")
    elif(e<E and s>S  and d>D and c>C):
        print("you can't make a call please top up")
        print("sms can't sent messagefailed")
        print("your data speed decreases as you exceed your limit")
elif(e>E):
    print("plan expired")
        
