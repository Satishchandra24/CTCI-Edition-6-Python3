"""There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple-> true
pales, pale -> true
pale,bale-> true
pale,bake-> false"""

def oneAway(str1,str2): #In this function based on the length of the str2 comapared to str1 one we will call delete,replace or insert
    len1=len(str1)
    len2=len(str2)
    if len1==len2+1:
        return checkDelete(str1,str2)
    elif len1==len2:
        return checkReplace(str1,str2)
    elif len1==len2-1:
        return checkInsert(str1,str2)
    else:
        return False
def checkDelete(str1,str2):#This function will see if two strings are same after we delete on char
    a={}#define map
    b={}
    for i in range(len(str1)):
        a[i]=str1[i] #In this map we will have key->val pair For the first string 1->'first char in string' ...
    for i in range(len(str2)):#In this map we will have key->val pair for the second string
        if str1[i]==str2[i]:#We will add a char at pos i if the char at the position is same as in str1
            b[i]=str2[i]
        else:
            b[i+1]=str2[i]#We will add the char at pos i+1 since it will be same at that pos
    count=0
    for i in b.keys():
        try:
            if b[i]==a[i]:
                count=count+1
        except:
            return False
    if count==len(str2): #We will count the same vals for keys in both map and return true if the count is same
        return True
    return False
def checkInsert(str1,str2):
    a={}
    b={}
    for i in range(len(str1)):
        #a[str1[i]]=i
        a[i]=str1[i]
    for i in range(len(str2)):
        if i==len(str2)-1:
            b[i]=str2[i]
            break
        if str1[i]==str2[i]:
            #b[str2[i]]=i
            b[i]=str2[i]
        else:
            #b[str2[i]]=i+1
            b[i]=str2[i+1]
    count=0
    print(a)
    print(b)
    for i in b.keys():
        try:
            if b[i]==a[i]:
                count=count+1
        except:
            pass
    print(count)
    if count==len(str2)-1:
        return True
    return False
def checkReplace(str1,str2):
    a={}
    b={}
    for i in range(len(str1)):
        a[i]=str1[i]
    for i in range(len(str2)):
        if str1[i]==str2[i]:
            b[i]=str2[i]
        else:
            #b[str2[i]]=i+1
            b[i]=str2[i]
    count=0
    for i in b.keys():
        try:
            if b[i]==a[i]:
                count=count+1
        except:
            pass
    if count==len(str2)-1:
        return True
    return False
str1="ppqr"
str2="pppr"
output=oneAway(str1,str2)
if output:
    print("Yes they are on edit away")
else:
    print("No, they are not one edit away")
