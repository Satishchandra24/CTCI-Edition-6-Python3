"""Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack)"""


#Note this is not a complete solution complete it later

class SetOfStacks:
    def __init__(self,mainarr):
        self.mainarr=mainarr
def push(st,setarr,data,threshold):
    setarr.append(data)
    if len(setarr)==threshold:
        st.mainarr.append(setarr)
        setarr=[]
        return setarr
    return setarr

def pop(st,setarr):
    if len(setarr)==0:
        if st.mainarr[len(st.mainarr)-1]!=[]:
            st.mainarr[len(st.mainarr)-1].pop()
        else:
            st.mainarr.pop()
            st.mainarr[len(st.mainarr)-1].pop()
    else:
        setarr.pop()
    return setarr
def peek(st,setarr):
    if len(setarr)==0:
        if len(st.mainarr)>1:
            return st.mainarr[len(st.mainarr)-1][len(st.mainarr[len(st.mainarr)-1])-1]
        else:
            return st.mainarr[0][len(st.mainarr[0])-1]
    else:
        return setarr[len(setarr)-1]
setarr=[]
mainarr=[]
threshold=5
stack=SetOfStacks(mainarr)
setarr=push(stack,setarr,1,threshold)
setarr=push(stack,setarr,2,threshold)
setarr=push(stack,setarr,3,threshold)
setarr=push(stack,setarr,4,threshold)
setarr=push(stack,setarr,5,threshold)
setarr=push(stack,setarr,6,threshold)
setarr=push(stack,setarr,7,threshold)
setarr=push(stack,setarr,8,threshold)
setarr=push(stack,setarr,9,threshold)
setarr=push(stack,setarr,10,threshold)
setarr=pop(stack,setarr)
setarr=pop(stack,setarr)
setarr=pop(stack,setarr)
setarr=pop(stack,setarr)
setarr=pop(stack,setarr)
#setarr=pop(stack,setarr)
print(peek(stack,setarr))
