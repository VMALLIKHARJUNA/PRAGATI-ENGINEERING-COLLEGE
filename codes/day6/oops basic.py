class abc:
    var=10
obj=abc()
print(obj.var)

class abc:
    attribute=10
    def display(self):
        print("This is in class")
obj=abc()
print(obj.attribute)
obj.display()
