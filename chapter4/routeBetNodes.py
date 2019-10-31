"""Given a directed graph, design an algorithm to find out whether there is a
route between two nodes."""
from collections import deque
class Node:
    def __init__(self,key,visited=False):
        self.val=key
        self.adjacent=[]
        self.visited=visited


def addEdge(vertex1,vertex2):
    vertex1.adjacent.append(vertex2)


def routeBetNodesDFS(start,end):#This is the depth first implementation
    stack=[]
    #Vist the start vertex mark it visited and push it
    stack.append(start)
    start.visited=True
    flag=0
    while flag==0:
        startAdjLen=len(start.adjacent)
        if startAdjLen>=1:
            for i in range(len(start.adjacent)):
                if start.adjacent[i].visited==False and i<=startAdjLen:
                    stack.append(start.adjacent[i])
                    start.adjacent[i].visited=True
                    start=start.adjacent[i]
                    if start.val==end.val:
                        return True
                    flag=2
                    break
                else:
                    pass
        if flag!=2:
            if stack==[]:
                flag=1
            else:
                start=stack.pop()
        else:
            flag=0
    return False

def routeBetNodesBFS(start,end):
     queue=deque([])
     queue.append(start)
     start.visited=True
     flag=0
     while flag==0:
         startAdjLen=len(start.adjacent)
         if startAdjLen >=1:
             for i in range(len(start.adjacent)):
                 if start.adjacent[i].visited==False:
                     if start.adjacent[i].val == end.val:
                         return True
                     queue.append(start.adjacent[i])
                     start.adjacent[i].visited=True

                 else:
                     pass
         if queue==deque([]):
             flag=1
         else:
             start=queue.popleft()
     return False

start=Node("S")
v1=Node("A")
v2=Node("B")
v3=Node("C")
v4=Node("D")
v5=Node("E")
v6=Node("F")
v7=Node("G")

addEdge(start,v1)
addEdge(start,v2)
addEdge(start,v3)
addEdge(v1,v4)
addEdge(v4,v7)
addEdge(v7,v5)
addEdge(v5,v2)
addEdge(v7,v6)
addEdge(v6,v3)
#print("Check the route between using the depth first search ",start.val," and ",v6.val)
#print(routeBetNodesDFS(start,v6))

print("Check the route between using the breadth first search ",start.val," and ",v6.val)
print(routeBetNodesBFS(start,v6))
