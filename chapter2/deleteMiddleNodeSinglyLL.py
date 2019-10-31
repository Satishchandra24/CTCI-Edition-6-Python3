#Implement an algorithm to delete a node in the middle (i.e., any node but
#the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
#that node.

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

def delete(root,key): #This function only deletes the middle element, it does not delete the first and the last element
    curr=root
    prev=curr
    while curr:
        if curr.data==key:
            prev.next=curr.next
            #curr.next=prev
            return
        prev=curr
        curr=curr.next
node=Node(1)
insertion(node,2)
insertion(node,3)
insertion(node,4)
print("Before delete")
display(node)
delete(node,3)
print("After delete")
display(node)
