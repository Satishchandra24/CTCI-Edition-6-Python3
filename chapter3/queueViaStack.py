#Implement a MyQueue class which implements a queue using two stacks.

class Stack:
    def __init__(self,arr):
        self.arr=arr


def push(st,data):
    st.arr.append(data)
def pop(st):
    if len(st.arr)!=0:
        st.arr.pop()

def peek(st):
    if len(st.arr)!=0:
        return st.arr[len(st.arr)-1]

def enqueue(st1,st2,data): # st1 will hold the queue data and st2 can be used to covert stack to queue
    while peek(st1):#This loop will add all the elements of stack1 to stack2 so that we can insert the new data at the bottom of stack1
         push(st2,peek(st1))
         pop(st1)
    push(st1,data) # We insert the data at bottom of the stack1
    while peek(st2):#This loop will add back all the elements to stack1 from stack2 such that the queue property will remain intact
        push(st1,peek(st2))
        pop(st2)

def dequeue(st): # Since we have the stack1 as queue we can just pop the top element to dequeue the stack1
    if len(st.arr)!=0:
        st.arr.pop()
arr1=[]
arr2=[]

st1=Stack(arr1)
st2=Stack(arr2)

enqueue(st1,st2,1)
enqueue(st1,st2,2)
enqueue(st1,st2,3)
enqueue(st1,st2,4)
print(peek(st1))
dequeue(st1)
print(peek(st1))
