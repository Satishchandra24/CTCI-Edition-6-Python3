#Given a circular linked list, implement an algorithm that returns the node at the
#beginning of the loop.

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


def insertionCircular(root,data):
    curr=root
    node=Node(data)
    if curr.next==root:
        curr.next=node
        node.next=root
        return
    while curr.next!=root:
        curr=curr.next
    curr.next=node
    node.next=root

def display(root):
    curr=root
    while curr.next!=root:
        print(curr.data)
        curr=curr.next
    print(curr.data)

def loopDetection(root): # To detect a loop we just have to check if the next element is root, if that is satisfied we got the last element in the loop
    curr=root
    while curr.next!=root:
        curr=curr.next
    print(curr.data)
node=Node(1)
node.next=node

insertionCircular(node,2)
insertionCircular(node,3)
insertionCircular(node,4)
insertionCircular(node,5)
insertionCircular(node,6)

#display(node)
loopDetection(node)
