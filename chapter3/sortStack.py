"""Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. """

class Stack:
    def __init__(self,arr):
        self.arr=arr



def pushSort(st1,st2,data):
    if isNotEmpty(st1):
        while True:
            if isNotEmpty(st1):
                if peek(st1)<=data:
                    push(st2,peek(st1))
                    pop(st1)
                else:
                    break
            else:
                break
        push(st1,data)
        while isNotEmpty(st2):
            push(st1,peek(st2))
            pop(st2)
    else:
        st1.arr.append(data)
        return


def push(st,data):
    st.arr.append(data)

def pop(st):
    if isNotEmpty(st):
        st.arr.pop()
def peek(st):
    if isNotEmpty(st):
        return st.arr[len(st.arr)-1]


def isNotEmpty(st):
    if len(st.arr)!=0:
        return True
    else:
        return False


arr1=[]
st1=Stack(arr1)

arr2=[]
st2=Stack(arr2)

pushSort(st1,st2,1)
pushSort(st1,st2,8)
pushSort(st1,st2,4)
pushSort(st1,st2,3)
pushSort(st1,st2,2)
pushSort(st1,st2,1)
pop(st1)
pop(st1)
pushSort(st1,st2,100)
print(arr1)
