import sys

def minsteps(n,dp):

    if n == 1:
        return 0
    ans1 = sys.maxsize
    if n%3 == 0:
        if dp[n//3] == -1:
            ans1 = minsteps(n//3,dp)
            dp[n//3] = ans1
        else:
            ans1 = dp[n-1] 

    ans2 = sys.maxsize
    if n%2 == 0:
        if dp[n//2] == -1:
            ans2 = minsteps(n//2,dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]

    if dp[n-1] == -1:
        ans3 = minsteps(n-1,dp)
        dp[n-1] = ans3
    else:
        ans3 = dp[n-1]

    ans = 1 + min(ans1,ans2,ans3)
    return ans

n = int(input("Enter a number "))
dp = [-1 for i in range(n+1)]
print(f"minimum steps to {n} is {minsteps(n,dp)}")