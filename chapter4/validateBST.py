"""Implement a function to check if a binary tree is a binary search tree. """

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

def validateBST(root,min,max):
    if root==None:
        return True
    if (min!=None and root.val<min) or (max!=None and root.val>max):
        return False
    if (not validateBST(root.left,min,root.val)) or (not validateBST(root.right,root.val,max)):
        return False
    return True

#Here we manually build the binary tree
root=TreeNode(8)

curr=insertion(3)
root.left=curr
curr.parent=root

curr=insertion(10)
root.right=curr
curr.parent=root

curr=insertion(1)
root.left.left=curr
curr.parent=root.left

curr=insertion(6)
root.left.right=curr
curr.parent=root.left

curr=insertion(9)
root.right.left=curr
curr.parent=root.right

curr=insertion(14)
root.right.right=curr
curr.parent=root.right


inOrderTraversal(root,0)
print(validateBST(root,None,None))
