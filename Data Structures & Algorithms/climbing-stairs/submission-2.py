class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper([1,2],n)

    def helper(self, lis, n):
        while len(lis) < n:
            lis.append(lis[-1] + lis[-2])
        return lis[n - 1]
        