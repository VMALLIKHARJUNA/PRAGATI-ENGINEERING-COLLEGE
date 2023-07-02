""" binary tree traversal
1.inorder:-left-root-right (L-D-R)
2.preorder:- root-left-right (D-L-R)
3.postorder:-left-right-root (L-R-D)
                            A
                            |
                   --------- ----------
                   |                   |
                   B                   C
                   |                   |
              ----- -------     ------- ---------
             |             |    |               |
             D             E    F               G
Inorder traversal:- D B E A F C G
                            15
                            |
                   --------- ----------
                   |                   |
                   24                  54
                   |                   |
              -----              ------- ---------
             |                   |               |
             35                 62               13

Inorder traversal:- 35 24 15 62 54 13


                            45
                            |
                   --------- ----------
                   |                   |
                   25                  75
                   |                    
              ----- -------      
             |             |                     
             15            35                   

Preorder traversal:- 45 25 15 35 75

                      (1)
                      /\
                     /  \
                    /    \
                   (2)   (3)
                   /\     /\
                  /  \   /  \
                (4)  (5)(6) (7)
                     /      / \
                    /      /   \
                   (8)    (9)  (10)

Preorder traversal:- 1 2 4 5 8 3 6 7 9 10


                      (1)
                      /\
                     /  \
                    /    \
                   (2)   (3)
                   /\     /\
                  /  \   /  \
                (4)  (5)(6) (7)

Postorder traversal:- 4 5 2 6 7 3 1"""

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #First recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end=" ")
        #now recur on right child
        printInorder(root.right)
#FUNCTION-POSTORDER
def printPostorder(root):
    if root:
        #First recur on left child
        printPostorder(root.left)
        #now recur on right child
        printPostorder(root.right)
        #then print the data of node
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        #First print the data of node
        print(root.val,end=" ")
        #Then recur on left child
        printPreorder(root.left)
        #Finally recur on right child
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE-ORDER:")
printPreorder(root)
print()
print("INORDER:")
printInorder(root)
print()
print("POSTORDER:")
printPostorder(root)
























                      













