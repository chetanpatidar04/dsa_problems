# Reverse a String using Stack
# Last Updated : 23 Jul, 2025
# Given a string str, the task is to reverse it using stack. 

# Example:

# Input: s = "GeeksQuiz"
# Output: ziuQskeeG

# Input: s = "abc"
# Output: cba


def revsers(s):
    li = list(s)
    final_list = []
    for i in range(len(li)):        
        temp = li.pop()
        final_list.append(temp)
    final_str = "".join(final_list)
    return final_str


s = "GeeksQuiz"
print(revsers(s))
