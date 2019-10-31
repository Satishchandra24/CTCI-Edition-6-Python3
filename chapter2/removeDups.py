#Write code to remove duplicates from an unsorted linked list
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self,newNext):
        self.next=newNext

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertion(self,data):#adds element and the beginning of the list
        node1=Node(data)
        node1.setNext(self.head)
        self.head=node1
    def delete(self,key):#deletes the element using the given key
        curr=self.head
        prev=curr
        if curr.data==key:#deletes if the element is the first element in the linked list
            curr=self.head
            temp=curr.getNext()
            self.head=temp
            return
        while curr:
            if curr.getData()==key:
                temp=curr.getNext()
                prev.setNext(temp)
                break
            prev=curr
            curr=curr.getNext()
    def display(self):#Displays all the elements in the list
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.getNext()
    def removeDups(self):
        curr=self.head
        hashMap={}
        index=0
        hashMap[index]=curr.data
        curr=curr.getNext()
        while curr!=None:
            index=index+1
            for i in hashMap.keys():
                if hashMap[i]==curr.data:
                    print("Hello",curr.data)
                    self.delete(curr.data)
                    break
            hashMap[index]=curr.data
            curr=curr.getNext()
l1=LinkedList()
l1.insertion(0)
l1.insertion(2)
l1.insertion(3)
l1.insertion(0)
l1.insertion(5)
l1.insertion(5)
l1.insertion(9)
l1.insertion(9)
l1.display()
l1.removeDups()
l1.display()
