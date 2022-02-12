
#Solve with List
# Problem also could be solved with Queue and Deque
from queue import Queue


userInput = input("Please provide parantheses to validate:")
openingBrackets = ["(", "{", "["]
closingBrackets = [")", "}", "]"]

def isBracketsBalanced(expression):
    stack = []
    
    #Loop through given expression
    for char in expression:
        #if it is an opening bracket
        if char in openingBrackets:
            stack.append(char)
        else:
            #if not an opening brackets
            #then should be a closing bracket
            #in this case stack should have at least one opening bracket
            #in other words can not be empty
            if not stack:
                return False

            if char not in closingBrackets:
                return False

            last_char = stack.pop()

            if last_char == "(":
                if char != ")":
                    return False
            if last_char == "{":
                if char != "}":
                    return False   
            if last_char == "[":
                if char != "]":
                    return False              

    if stack:
        return False
    return True

if isBracketsBalanced(userInput):
    print("Balanced")
else:
    print ("Not Balanced")    
