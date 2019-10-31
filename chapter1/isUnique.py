#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(inputString):
    if len(inputString)>128:
        return False
    char_check=[False for i in range(128)]# This will hold 128 False values as the array
    for i in range(len(inputString)):
        val=ord(inputString[i]) # This ord function gives us the value of the character unicode of that charcter
        if char_check[val]:
            return False
        char_check[val]=True
    return True
input="1!!"
output=isUnique(input)
if output:
    print("All the characters in the string is unique")
else:
    print("All the characters in the string are not unique")
