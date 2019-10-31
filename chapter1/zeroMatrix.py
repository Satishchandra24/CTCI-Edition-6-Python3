
#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#column are set to O
# This code works for only first 0 it finds, make a generic to finad all zero's and get the row col zero
def zeroMatrix(inputMatrix):
    len1=len(inputMatrix)
    for i in range(len1):
        len2=len(inputMatrix[i])
        for j in range(len2):
            if inputMatrix[i][j]==0:
                setRowZero(i,j,len1,len2,inputMatrix)
                setColZero(i,j,len1,len2,inputMatrix)
                return inputMatrix
    return inputMatrix
def setRowZero(i,j,len1,len2,inputMatrix):
    curr=0
    while curr!=len2:
        inputMatrix[i][curr]=0
        curr=curr+1
def setColZero(i,j,len1,len2,inputMatrix):
    curr=0
    while curr!=len1:
        inputMatrix[curr][j]=0
        curr=curr+1


print("Input: ")

input=[[1,2,3,4],[4,0,6,7],[7,8,9,10]]
for i in range(len(input)):
    for j in range(len(input[i])):
        print(input[i][j],end=" ")
    print("     ")
output=zeroMatrix(input)

print("Output: ")
for i in range(len(output)):
    for j in range(len(output[i])):
        print(output[i][j],end=" ")
    print("     ")
