#Describe how you could use a single array to implement three stacks.
#Finsh this later with the dynamic and static array
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
        print(st.arr[len(st.arr)-1])

arr=[None]*6
print(arr)
st1=Stack(arr,)
st2=Stack(arr)
st3=Stack(arr)
push(st1,1)
push(st1,2)
push(st2,1)
#pop(st1)
peek(st1)
