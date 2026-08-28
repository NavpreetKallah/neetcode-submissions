class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        def backtrack(i, curr):
            if i == len(nums):
                return False
            if curr + nums[i] == target:
                return True
            valid = False
            if curr + nums[i] < target:
                valid = valid or backtrack(i + 1, curr + nums[i])
            valid = valid or backtrack(i + 1, curr)
            return valid
        return backtrack(0, 0)
        