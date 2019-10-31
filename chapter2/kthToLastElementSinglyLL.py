#Implement an algorithm to find the kth to last element of a singly linked list.

class Node: #This is the node class for each node in linked list
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def insertion(root,data): #this function implements the insertion of the new element in linked list
    curr=root
    node=Node(data)
    if curr.next==None:
        curr.next=node
        node=curr
        return
    while curr.next!=None:
        curr=curr.next
    curr.next=node
    node=curr
def display(root):#This function will print all the nodes in the linked list
    curr=root
    while curr:
        print(curr.data)
        curr=curr.next
def returnKthToLast(root,k): #This funciton will print the kth to last element in the linked list
    curr=root
    counter=1
    while curr:
        if counter>=k:
            print(curr.data)
        curr=curr.next
        counter=counter+1



node=Node(1)
insertion(node,2)
insertion(node,3)
insertion(node,4)
insertion(node,5)
#display(node)
returnKthToLast(node,1)
