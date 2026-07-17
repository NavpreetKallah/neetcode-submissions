class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for index in range(len(nums) + 1):
            if index not in nums:
                return index