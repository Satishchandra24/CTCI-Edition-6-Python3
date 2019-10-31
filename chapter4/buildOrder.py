"""You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error. """
# I was able to find the solution to the given input but was not able to understand the return error thing
class Node:
    def __init__(self,key,visited=False,isLinked=False,dependent=None):
        self.val=key
        self.dependent=dependent
        self.visited=visited
        self.isLinked=isLinked



def buildGraph(dependencies,nodes):
    for i in range(len(dependencies)):
        iter=0
        j=0
        while True:
            if nodes[iter].val==dependencies[i][j]:
                vertex1=nodes[iter]
                break
            iter=iter+1
        iter=0
        j=1
        while True:
            if nodes[iter].val==dependencies[i][j]:
                vertex2=nodes[iter]
                break
            iter=iter+1
        addEdge(vertex1,vertex2)


def addEdge(vertex1,vertex2):#adds the edge between vertices
    vertex1.isLinked=True
    vertex2.isLinked=True
    vertex2.dependent=vertex1

def buildOrder1(nodes):
    for i in range(len(nodes)):
        curr=nodes[i]
        while curr.dependent!=None:
            curr=curr.dependent
        if curr.visited==False:
            print(curr.val)
        curr.visited=True
    for i in range(len(nodes)):
        curr=nodes[i]
        if curr.visited==False:
            if curr.dependent.visited==True:
                curr.visited=True
                print(curr.val)
    for i in range(len(nodes)):
        curr=nodes[i]
        if curr.visited==False:
            if curr.dependent.visited==True:
                print(curr.val)
def buildOrder(nodes,output,maxLen):
    length=len(nodes)
    i=0
    while i<length:
        curr=nodes[i]
        while curr.dependent!=None:
            curr=curr.dependent
        if curr.visited==False:
            #print(curr.val)
            output.append(curr.val)
        curr.visited=True
        i=i+1
    return output
def buildRemOrder(nodes,output,maxLen):
    length=len(nodes)
    i=0
    while True:
        if len(output)==maxLen:
            break
        if i==length-1:
            i=0

        curr=nodes[i]

        if curr.visited==False:
            if curr.dependent.visited==True:
                curr.visited=True
                output.append(curr.val)
                #print(curr.val)
        i=i+1
    return output
# We get two inputs here the first one is projects and the second one is the dependencies

projects=["a","b","c","d","e","f"]
dependencies=[["a","d"],["f","b"],["b","d"],["f","a"],["d","c"]]

# The first i will do is build the graph based on the dependencies
#In order to build the graph i would need nodes of all the project(even if it dont use them it will generate them)
nodes=[]
for i in range(len(projects)):
    node=Node(projects[i])
    nodes.append(node)
buildGraph(dependencies,nodes)

#Once we build the graph using the is build factor and no dependencies we cal add those nodes in order
output=[]
maxLen=len(nodes)
output=buildOrder(nodes,output,maxLen)
#Next we will build the remaing nodes which were dependent
output=buildRemOrder(nodes,output,maxLen)
print(output)
