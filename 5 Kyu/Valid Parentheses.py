"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

def valid_parentheses(string):
    parentheses = [i for i in string if i == "(" or i == ")"]
    if len(parentheses) == 0:
        return True
    elif len(parentheses) == 1:
        return False
    elif parentheses[0] == ")" or parentheses[len(parentheses)-1] == "(":
        return False
    else:
        for i in range(len(parentheses)):
            if parentheses[i] == '(':
                parentheses.pop(i)
                break
        for j in range(len(parentheses)):
            if parentheses[j] == ')':
                parentheses.pop(j)
                break
        return valid_parentheses(parentheses)
