# Given a string s representing an expression containing various types of brackets: {}, (), and [], the task is to determine whether the brackets in the expression are balanced or not. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.

# Example: 

# Input: s = "[{()}]"
# Output: true
# Explanation:  All the brackets are well-formed.

# Input: s = "[()()]{}"
# Output: true
# Explanation: All the brackets are well-formed.

# Input: s = "([]"
# Output: false
# Explanation: The expression is not balanced as there is a missing ')' at the end.

# Input:  s = "([{]})"
# Output: false
# Explanation: The expression is not balanced because there is a closing ']' before the closing '}'.


s = "[]"
di = {"{":"}","[":"]","(":")"}
li = []

def validate_string(s):
    if len(s) <= 1:
        return "Invalid"
    for i in s:
        if i in di.keys():
            li.append(i)
        else:
            if len(li) > 0:
                print(li[-1],"temo")
                print(di[li[-1]],"this is")
                if di[li[-1]] == i:
                    li.pop()
        
    if len(li) == 0:
        return "Valid string"
    return "Invalid  strngd "

print(validate_string(s))