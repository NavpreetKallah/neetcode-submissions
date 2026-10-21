class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        self.n = len(nums)
        for i in range(1, self.n + 1):
            if self.subArraySum(target, nums, i):
                return i
        return 0

    def subArraySum(self, target, nums, k):
        for i in range(self.n - k + 1):
            if sum(nums[i:i+k]) >= target:
                return True
        return False