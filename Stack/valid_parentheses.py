# Optimized solution

def isValid(s: str) -> bool:
    stack = []
    match = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
        if c in match:
            if stack and stack[-1] == match[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False
    
# solutin 2

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char == '(' or  char=='{' or char=='[':
                stack.append(char)
     
            else:
                if not stack: #stack is empty
                    return False
                if char==')' and stack[-1]=='(':
                    stack.pop()
                elif char=='}'and stack[-1]=='{':
                    stack.pop()
                elif char==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        return  not stack