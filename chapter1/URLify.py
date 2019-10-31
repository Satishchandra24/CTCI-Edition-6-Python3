#Write a method to replace all spaces in a string with '%20: You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string
#Since in python we cannot change the string by assignment I have used an extra temp variable though I could use replace
def urlIFY(inputString):
    temp=""
    for i in range(len(inputString)):
        if inputString[i]!=' ':
            temp=temp+inputString[i]
        else:
            temp=temp+'%20'
    return temp
input="Mr John Smith"
output=urlIFY(input)
print(output)
