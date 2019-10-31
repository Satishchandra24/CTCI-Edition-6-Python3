"""Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)ndrome does not need to be limited to just dictionary words.    """

def permutationPalindrome(inputString):
    print(inputString)
    a={}#Declare the hash table
    for i in range(len(inputString)):#Add 0s as value for each key
        a[inputString[i]]=0
    for i in range(len(inputString)):#Change the value of each key to its count
        a[inputString[i]]=a[inputString[i]]+1
    counter=0
    for i in a.keys():# check if you have two or more keys with count value 1
        if a[i]==1:
            counter=counter+1
    if counter<=1: # If you get the one or less keys with count value 1 it is palindrome else it is not
        return True
    print(a)
    return False

input="tactoca"
output=permutationPalindrome(input)
if output:
    print("The permutation of the input string is palindrome")
else:
    print("The permutation of the input string is not palindrome")
