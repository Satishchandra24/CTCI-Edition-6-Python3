#Describe how you could use a single array to implement three stacks

class Stack:
    def __init__(self,arr):
        self.arr=arr



def push(st,data,stMin):
    st.arr.append(data)
    addMin(data,stMin)


def pop(st,stMin):
    if len(st.arr)!=0:
        delMin(peek(st),stMin)
        st.arr.pop()


def peek(st):
    if len(st.arr)!=0:
        return st.arr[len(st.arr)-1]
def addMin(data,stMin):
    if len(stMin.arr)!=0:
        if peek(stMin)>=data:
            stMin.arr.append(data)
    else:
        stMin.arr.append(data)
def delMin(data,stMin):
    if data==peek(stMin):
        stMin.arr.pop()
def checkMin(stMin):
    if len(stMin.arr)!=0:
        return stMin.arr[len(stMin.arr)-1]



arr=[]
arrMin=[]
st=Stack(arr)
stMin=Stack(arrMin)
push(st,4,stMin)
push(st,3,stMin)
push(st,2,stMin)
push(st,1,stMin)
pop(st,stMin)
pop(st,stMin)
pop(st,stMin)
print(checkMin(stMin))
