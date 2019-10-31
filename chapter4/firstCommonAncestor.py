"""Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree. """

#Lets assume we know the parents of the node in the given binary tree

class TreeNode:# This node is to store the tree data
    def __init__(self,key,left=None,right=None,parent=None,depth=0):
        self.val=key
        self.left=left
        self.right=right
        self.parent=parent

def insertion(key): #This function will insert the data in the tree
    return TreeNode(key)

def inOrderTraversal(root,space):# This is not inorder, it is just used to print the tree
    if root!=None:
        inOrderTraversal(root.right,space+5)
        for i in range(space):
            print(end=" ")
        print (root.val)
        inOrderTraversal(root.left,space+5)


def firstCommonAncestor1(node1,node2):
    print(node1.val)
    print(node2.val)
    while True:
        parent1=node1.parent
        if parent1==node2.parent:
            return parent1
        parent2=node2.parent
        if parent1==parent2:
            return parent2
        node1=parent1
        node2=parent2
def firstCommonAncestor(node1,node2):
    print(node1.val)
    print(node2.val)
    while True:
        if node1.parent!=None and node2.parent!=None:
            if node1.parent==node2:
                return node2
            if node2.parent==node1:
                return node1
        if node1.parent!=None:
            parent1=node1.parent
        else:
            parent1=node1
        if node2.parent!=None:
            parent2=node2.parent
        else:
            parent2=node2
        if parent1==parent2:
            return parent2
        node1=parent1
        node2=parent2

#Here we manually build the binary tree
root=TreeNode(1)

curr1=insertion(2)
root.left=curr1
curr1.parent=root

curr2=insertion(3)
root.right=curr2
curr2.parent=root

curr3=insertion(4)
root.left.left=curr3
curr3.parent=root.left

curr4=insertion(5)
root.left.right=curr4
curr4.parent=root.left

curr5=insertion(6)
root.right.left=curr5
curr5.parent=root.right

curr6=insertion(7)
root.right.right=curr6
curr6.parent=root.right


inOrderTraversal(root,0)
print(firstCommonAncestor(root,curr2).val)
