def removeOuterParentheses(s: str) -> str:

    n = len(s)
    st = 0
    l = 0
    o = 0
    string = ""
    for i in range(n):
        if s[i] == '(':
            l+=1
        else:
            o+=1
        if l == o:
            string+=str(s[st+1:i])
            st = i+1
    return string