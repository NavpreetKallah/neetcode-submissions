class Solution:
    def __init__(self) -> None:
        self.dp = [0] * 38
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 1

    def tribonacci(self, n: int) -> int:
        for i in range(3,n+1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2] + self.dp[i - 3]
        return self.dp[n]