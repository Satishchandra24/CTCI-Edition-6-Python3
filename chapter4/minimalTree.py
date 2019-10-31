#Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
import math
class Node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key=key
        self.left=left
        self.right=right
        self.parent=parent


def generateTree(arr,start,end):
    if end<start:
        return
    mid=math.floor((start+end)/2)
    node=Node(arr[mid])
    print("1->",node.key)
    node.left=generateTree(arr,start,mid-1)
    print("2->",node.key)
    node.right=generateTree(arr,mid+1,end)
    print("3->",node.key)
    return node

def inOrderTraversal(root,space):# This is not inorder, it is just used to print the tree
    if root!=None:
        inOrderTraversal(root.right,space+5)
        for i in range(space):
            print(end=" ")
        print (root.key)
        inOrderTraversal(root.left,space+5)

arr=[1,2,3,4,6,7,8]
n=len(arr)
#First we will get the root element which is the mid element of the array
#node=Node(arr[math.floor(n/2)])
node=generateTree(arr,0,n-1)
inOrderTraversal(node,0)
