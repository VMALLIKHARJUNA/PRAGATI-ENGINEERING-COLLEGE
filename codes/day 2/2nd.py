email="surya@gmail.com"
pwd="p12345"
otp="1234"
cemail=input("enter the email:" )
cpwd=input("enter the pwd:")

if(email==cemail and pwd==cpwd):
    print("login sucessfully")
    x=input("enter otp:")
    if(x==otp):
        print("order placed suceefully")
    else:
        print("wrong otp entered")
elif(email==cemail or pwd==cpwd):
    print("login failed",end="-")
    if(email==cemail):
        print("wrong password")
    elif(pwd==cpwd):
        print("wrong email")
else:
    print("login failed wrong email and password")
