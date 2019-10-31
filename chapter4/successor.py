"""Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent """

class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.val=key
        self.left=left
        self.right=right
        self.parent=parent

def insertBST(root,key):
    node=Node(key)
    if node.val<=root.val:
        if root.left==None:
            root.left=node
            node.parent=root
            return node
        else:
            return insertBST(root.left,key)
    else:
        if root.right==None:
            root.right=node
            node.parent=root
            return node
        else:
            return insertBST(root.right,key)


def inOrderTraversal(root,space):# This is not inorder, it is just used to print the tree
    if root!=None:
        inOrderTraversal(root.right,space+5)
        for i in range(space):
            print(end=" ")
        print (root.val)
        inOrderTraversal(root.left,space+5)

def getSuccessor(node):
    if node.parent==None:
        if node.right!=None:
            return node.right
        else:
            return None
    else:
        par=node.parent
        if node==par.left:
            return par
        elif node==par.right:
            if par.parent!=None:
                if par.parent.left==par:
                    return par.parent
                else:
                    return None
            else:
                return None






root=Node(8)

node1=insertBST(root,3)
node2=insertBST(root,10)
node3=insertBST(root,1)
node4=insertBST(root,6)
node5=insertBST(root,9)
node6=insertBST(root,14)
inOrderTraversal(root,0)
#print(node3.parent.val)
output=getSuccessor(node1)
if output!=None:
    print("The successor is ",output.val)
else:
    print("There is no successor found")
