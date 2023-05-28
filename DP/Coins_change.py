def getCoins(coins, n, sum):
    dp = [[0 for i in range(n+1)] for j in range(sum+1)]
    for i in range(n+1):
        dp[0][i] = 1

    for i in range(sum+1):
        for j in range(n+1):
            dp[i][j] = dp[i][j-1]
            if coins[j-1] <= i:
                dp[i][j] += dp[i-coins[j-1]][j]
    
    return dp[sum][n]

if __name__ == "__main__":
    
    print(getCoins([1,2,3],3,4))