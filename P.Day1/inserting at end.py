#single linlked list inserting at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp= temp.next
        temp.next=ne

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
print("Before inserting 100")
obj.display()
print("")
print("After inserting 100")
obj.insert_end(100)
obj.display()
print("")









