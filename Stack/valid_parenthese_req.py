class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []
        for i in s:
            if len(arr)>0 and arr[-1]=='(' and i==")":
                arr.pop()
            else: 
                arr.append(i)

        return len(arr)