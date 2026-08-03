class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for index, num in enumerate(nums):
            if index >= 3:
                dp[index] += max(dp[index - 2], dp[index - 3]) + num
            elif index == 2:
                dp[index] = num + dp[index - 2]
            else:
                dp[index] = num

        print(dp)
        
        return dp[-1] if len(dp) == 1 else max(dp[-1], dp[-2])
        