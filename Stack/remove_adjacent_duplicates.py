class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            if len(arr)!=0 and arr[-1]==s[i]:
                arr.pop()
            else:
                arr.append(s[i])

        return "".join(arr)