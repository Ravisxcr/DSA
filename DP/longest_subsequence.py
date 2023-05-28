def lcs(x,y,s1,s2):
    dp = [[-1 for i in range(y+1)] for j in range (x+1)]
    
    for i in range(x+1):
        dp[i][0] = 0
    for j in range(y+1):
        dp[0][j] = 0
        
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i][j-1], dp[i-1][j])
    
    return dp[i][j]

if __name__ == "__main__":
    print(lcs(3,4,'qwe','qter'))