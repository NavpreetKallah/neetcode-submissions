class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1] * n for _ in range(m)]

        def move(i , j):

            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = move(i + 1, j) + move(i, j + 1)
            return dp[i][j]

        

        return move(0, 0)