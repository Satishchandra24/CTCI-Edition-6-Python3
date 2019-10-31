#You have two numbers represented by a linked list, where each node contains a single
#digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
#function that adds the two numbers and returns the sum as a linked list.
import math
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

def sumListReverse(node1,node2): # This function will take two linked list in reverse order add them and make a new linked list
    curr1=node1 # First LL
    curr2=node2 # second LL
    node=Node(0) # new node for the sum LL
    curr=node
    first=0 # Any sum starts with 0 and we add what ever we get from the list
    second=0
    fac=1 # This is as mulitiplication factor by which we mul each digit and add it to get the no in rev order
    while curr1:
        first=first+curr1.data*fac
        curr1=curr1.next
        fac=fac*10 # Increment the factor by 10
    fac=1
    while curr2:
        second=second+curr2.data*fac
        curr2=curr2.next
        fac=fac*10

    sum=first+second
    while sum!=0:
        curr.next=Node(math.floor(sum%10)) # add each right most digit to the linked list first so that we get the output in revere order
        curr=curr.next
        sum=math.floor(sum/10)
    print("The sum of above two list in reverse order is ")
    display(node.next) # We display it from the next to get the rid of temporary value that node holds at the defination

node1=Node(1)
insertion(node1,2)
insertion(node1,3)

node2=Node(4)
insertion(node2,5)
insertion(node2,9)


print("The first linked list in reverse order  is ")
display(node1)
print("The second linked list in reverse order is ")
display(node2)

sumListReverse(node1,node2)
