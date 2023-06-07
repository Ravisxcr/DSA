class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if m == 1 and n ==1:
            return grid[0][0]

        dp = [[0 for i in range(n)] for j in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for j in range(1,m):
            dp[j][0] = grid[j][0] + dp[j-1][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min((grid[i][j] + dp[i-1][j]), (grid[i][j] + dp[i][j-1]))

        return dp[m-1][n-1]