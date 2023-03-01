'''Write a program to check whether the given number is even/odd by using single stance class object with an attribute following the constructor
Test case1:i/p=21'''
class Number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num, "is =even")
        else:
            print(num,"is odd")
n=Number()
n.even_odd(21)
print()
###############
class Number:
    even=0
    def check(self,num):
        if num%2!=0:
            self.odd=1
    def even_odd(self,num):
        self.check(num)
        if self.odd==1:
            print(num, "is odd")
        else:
            print(num,"is even")
n=Number()
n.even_odd(21)
print()
################3
class Number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1=Number(11)
n2=Number(13)
n3=Number(12)
n4=Number(28)
n5=Number(7)
print(Number.even)
print(Number.odd)
print()
#############

