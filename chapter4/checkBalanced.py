""" Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one."""
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


def checkBalanced(root):
    if root==None:
        return True
    heightDiff=getHeight(root.left)-getHeight(root.right)
    if abs(heightDiff)>1:
        return False
    else:
        return checkBalanced(root.left) and checkBalanced(root.right)
def getHeight(root):
    if root==None:
        return -1
    else:
        return max(getHeight(root.left),getHeight(root.right))+1

#Here we manually build the binary tree
root=TreeNode(1)

curr=insertion(2)
root.left=curr
curr.parent=root

curr=insertion(3)
root.right=curr
curr.parent=root

curr=insertion(4)
root.left.left=curr
curr.parent=root.left

curr=insertion(5)
root.left.right=curr
curr.parent=root.left

curr=insertion(6)
root.right.left=curr
curr.parent=root.right

curr=insertion(7)
root.right.right=curr
curr.parent=root.right


inOrderTraversal(root,0)
print(checkBalanced(root))
