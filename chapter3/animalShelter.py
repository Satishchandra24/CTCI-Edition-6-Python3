""" An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure. """

class Node:
    def __init__(self,key,next=None):
        self.type=key
        self.next=next

def enqueue(root,key): #Since it is first in first out the root element will go out
    node=Node(key)
    curr=root
    if curr.next==None:
        curr.next=node
        return
    while curr.next!=None:
        curr=curr.next

    curr.next=node
    return


def dequeueAny(root):#This will remove the first node in the list since we can deque any type based on its arrival
    curr=root
    if curr.next!=None:
        curr=curr.next
        #root=curr
        return curr
    return

def dequeueCat(root,type="cat"):#Here we just have to deque the oldest cat, to do this we can go over the LL and see if we could get the oldest cat
    curr=root
    if curr.type==type: # If the head of LL is cat return it
        print("You got the Cat")
        return dequeueAny(curr)
    else: # We check for cat and do the node deletion that is why we need prev node and we link it with the curr.next
        prev=curr
        while curr.next.type!=type:
            prev=curr
            curr=curr.next
            if curr.next==None:
                print("No cat availabe")
                return root
        prev=prev.next
        curr=curr.next
        prev.next=curr.next
        return root
def dequeueDog(root,type="dog"):
    curr=root
    if curr.type==type:
        print("You got the dog")
        return dequeueAny(curr)
    else:
        prev=curr
        while curr.next.type!=type:
            prev=curr
            curr=curr.next
            if curr.next==None:
                print("No dog availabe")
                return root
        prev=prev.next
        curr=curr.next
        prev.next=curr.next
        return root

def display(root):
    curr=root
    while curr:
        print(curr.type)
        curr=curr.next


node=Node("dog")
enqueue(node,"cat")
enqueue(node,"cat")
enqueue(node,"dog")
enqueue(node,"dog")
enqueue(node,"cat")
enqueue(node,"dog")
node=dequeueDog(node)
#node=dequeueDog(node)
#node=dequeueDog(node)
#node=dequeueDog(node)
#node=dequeueCat(node)
#node=dequeueCat(node)
#node=dequeueCat(node)
#display(node)
