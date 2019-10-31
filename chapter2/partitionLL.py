#Write code to partition a linked list around a value x, such that all nodes less than x come
#before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
#to be after the elements less than x (see below) . The partition element x can appear anywhere in the
#"right partition"; it does not need to appear between the left and right partitions.


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

def partitionLL(root,key): #This function will divide the linked list in such a way that everything less the key will come before everything that is greater
    node1=Node(0)#This node will hold the less values
    node2=Node(0)#This node will hold the greater values
    curr1=node1#curr value for less LL
    curr2=node2#curr value for more LL
    curr=root#curr value for the give LL
    while curr:
        if curr.data<key:#If the values is less than key add it to first LL
            curr1.next=Node(curr.data)
            curr1=curr1.next
        elif curr.data>=key:#if the value is greater than the key add it to second LL
            curr2.next=Node(curr.data)
            curr2=curr2.next
        curr=curr.next
    curr1.next=node2.next #this connect the last element of the first list to second element of the second list (first ele of any node is 0 and we should remove them)
    display(node1.next) # We will start printing from the second element of the combined LL (first element is 0 and we should remove it)

node=Node(3)
insertion(node,5)
insertion(node,8)
insertion(node,5)
insertion(node,10)
insertion(node,2)
insertion(node,1)
#display(node)
partitionLL(node,5)
