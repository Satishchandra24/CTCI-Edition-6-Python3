#Implement a function to check if a linked list is a palindrome.
#In this approach we will reverse the linked list and compare both of them
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None

def insertion(root,data):
    curr=root
    node=Node(data)
    if curr.next==None:
        curr.next=node
        return
    while curr.next!=None:
        curr=curr.next
    curr.next=node

def display(root):
    curr=root
    while curr:
        print(curr.data)
        curr=curr.next

def checkPalindrome(root): #This fucntion will reverse the current linked list
    curr=root
    newroot=Node(0)
    curr2=newroot
    while curr:
        temp=Node(curr.data)
        temp.next=curr2
        curr=curr.next
        curr2=temp
    newroot=curr2
    return checkSimilar(root,newroot)

def checkSimilar(root,newroot): #This function will get both the new LL and old LL and check if they are same
    curr1=root
    curr2=newroot
    while curr1 and curr2:
        #print("curr1",curr1.data)
        #print("curr2",curr2.data)
        if curr1.data!=curr2.data:
            return False
        curr1=curr1.next
        curr2=curr2.next
    return True
node=Node(1)
insertion(node,2)
insertion(node,3)
insertion(node,2)
insertion(node,1)
#display(node)
output=checkPalindrome(node)
if output==True:
    print("YES, the linked list is a palindrome")
else:
    print("NO, the linked list is not a palindrome")
