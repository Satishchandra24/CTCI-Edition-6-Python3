"""Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists) """
class TreeNode:# This node is to store the tree data
    def __init__(self,key,left=None,right=None,parent=None,depth=0):
        self.val=key
        self.left=left
        self.right=right
        self.parent=parent

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


def insertion(key): #This function will insert the data in the tree
    return TreeNode(key)

def inOrderTraversal(root,space):# This is not inorder, it is just used to print the tree
    if root!=None:
        inOrderTraversal(root.right,space+5)
        for i in range(space):
            print(end=" ")
        print (root.val)
        inOrderTraversal(root.left,space+5)


def generateLL(root,llList,level):
    if root==None:
        return llList
    node=Node(root.val)

    tempList=[]
    tempList.append(node)
    listlen=len(llList)
    if listlen==0:
        llList.append(tempList)
    elif level==listlen:
        llList.append(tempList)
    elif level<listlen:
        curr=llList[level][0]
        while curr.next!=None:
            curr=curr.next
        curr.next=node
    generateLL(root.left,llList,level+1)
    generateLL(root.right,llList,level+1)
    return llList

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
llList=[]
output=generateLL(root,llList,0)
print("The output for the level wise linked list is")
for i in range(len(output)):
    print("Level",i)
    for j in range(len(output[i])):
        curr=output[i][j]
        while curr:
            print(curr.data)
            curr=curr.next
