def fib(n,dp):

    if n == 1 or n==0:
        return n
    
    if dp[n-1] == -1:
        ans1 = fib(n-1,dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    if dp[n-2] == -1:
        ans2 = fib(n-2,dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]

    return ans1 + ans2

n = int(input("Enter the number"))
dp = [-1 for i in range(n+1)]
print(f"The fibbonacci for {n} is {fib(n,dp)}")