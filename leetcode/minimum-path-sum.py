class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1,len(grid[0])):#fill first row
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1,len(grid)):#fill firs col
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1,len(grid)):# rows
            for j in range(1,len(grid[0])):#cols
                dp[i][j]= grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]