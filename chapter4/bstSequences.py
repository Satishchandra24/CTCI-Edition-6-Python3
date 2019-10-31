"""A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree. """
# This does not give all the values
class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.val=key
        self.left=left
        self.right=right
        self.parent=parent

def generateBST(root,inputArr):
    for i in range(1,len(inputArr)):
        insertBST(root,inputArr[i])


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


def bstSequences(root,outputArr,arr1,arr2,arr):
    #root left right
    if root.left==None and root.right==None:
        flag=0
        for i in range(len(outputArr)):

            if outputArr[i]==arr:
                flag=1
                break
        if flag==0:
            outputArr.append(arr)
    for i in range(len(arr)):
        arr1.append(arr[i])
        arr2.append(arr[i])
    if root.left!=None:
        arr1.append(root.left.val)

    if root.right!=None:
        arr1.append(root.right.val)

    if root.right!=None:
        arr2.append(root.right.val)

    if root.left!=None:
        arr2.append(root.left.val)
    if root.left!=None:
        bstSequences(root.left,outputArr,[],[],arr1)
        bstSequences(root.left,outputArr,[],[],arr2)
    if root.right!=None:
        bstSequences(root.right,outputArr,[],[],arr1)
        bstSequences(root.right,outputArr,[],[],arr2)
    return outputArr
def inOrderTraversal(root,space):# This is not inorder, it is just used to print the tree
    if root!=None:
        inOrderTraversal(root.right,space+5)
        for i in range(space):
            print(end=" ")
        print (root.val)
        inOrderTraversal(root.left,space+5)


inputArr=[10,8,15,6,9,17,1]
length=len(inputArr)
root=Node(inputArr[0])
generateBST(root,inputArr)
inOrderTraversal(root,0)
outputArr=[]
arr1=[]
arr2=[]
arr=[]
arr.append(root.val)


outputArr=bstSequences(root,outputArr,arr1,arr2,arr)
actualOutput=[]
maxLen=len(inputArr)
for i in range(len(outputArr)):
    if len(outputArr[i])==maxLen:
        actualOutput.append(outputArr[i])
print(actualOutput)
print(outputArr)
