#Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
#"compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression(inputStr):
    a=""
    currStr=inputStr[0]
    currCount=0
    i=0
    while i!=len(inputStr):
        if inputStr[i]!=currStr:
            a=a+currStr
            a=a+str(currCount)
            currStr=inputStr[i]
            currCount=0
        if i==len(inputStr)-1:
            a=a+currStr
            a=a+str(currCount+1)
        currCount=currCount+1
        i=i+1
    return a
input="fsdhfjk"
output=stringCompression(input)
print("The input is ",input)
print("__________________________")
print("The output is",output)
