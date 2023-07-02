"""types of trees
1. binary tree :- a node can have maximum 2 children
    i.full binary tree (0 or 2 child)
    ii.degenerate or pathological binary tree (0 or 1 child)
    iii.skewed binary tree (only one side left side or right side)
    
2. complet binary tree :- every level should be  fill or complete
                          in last level , if it is incomplete nodes should be present at exteam left side
perfect binary tree all the internal nodes which has 2 children and leaf nodes should be at the same level
 balanced tree :-for all the nodes  hight left sub tree - hight of right subtree can be 0 or 1
"""
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(18)

node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7

print("Root Node is:")
print(node1.data)

print("left chid of the node is:")
print(node1.leftChild.data)

print("right chid of the node is:")
print(node1.rightChild.data)

print("Node is:")
print(node2.data)

print("left chid of the node is:")
print(node2.leftChild.data)

print("right chid of the node is:")
print(node2.rightChild.data)

print("Node is:")
print(node3.data)

print("left chid of the node is:")
print(node3.leftChild.data)

print("right chid of the node is:")
print(node3.rightChild.data)

























