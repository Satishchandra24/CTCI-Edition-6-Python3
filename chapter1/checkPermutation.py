#Given two strings, write a method to decide if one is a permutation of the other.
#str1 is permutation of string 2 if they have the same no of characters and same characters in any order

#One method would be to sort both the strings and compare them
def checkPermutation1(str1,str2):
    print(str1)
    print(str2)
    print(sorted(str2))
    if len(str1)!=len(str2):
        return False

    if sorted(str1)==sorted(str2):
        return True
    return False

def checkPermutation(str1,str2):
    if len(str1)!=len(str2):
        return False
    a={}
    b={}
    count=0
    for i in range(len(str1)):
        a[str1[i]]=0
        b[str2[i]]=0
    for i in range(len(str1)):
        a[str1[i]]=a[str1[i]]+1
    for i in range(len(str2)):
        b[str2[i]]=b[str2[i]]+1
    if a==b:
        return True
    return False

str1="abca"
str2="baca"

output=checkPermutation(str1,str2)
if output:
    print("Str2 is the permutation of the str1")
else:
    print("Str2 is not the permutation of the str1")
