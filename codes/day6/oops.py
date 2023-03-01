class xyz:
    var=100
class abc:
    attribute=10
    def display(self):
        print("This is in class")
obj=abc()
print(obj.attribute)
obj.display()
print()
##################
class abc:
    def __init__(self,value):
        print("This is in class")
        self.value=value
        print("The value is:",value)
obj=abc(100)
print()
###################
class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("The obj value is:",var)
        print("The class value is:",abc.class_var)
obj1=abc(100)
obj2=abc(200)
obj3=abc(300)
