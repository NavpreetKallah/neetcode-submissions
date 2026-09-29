class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        while l < len(nums):
            if nums[l] == val:
                r = l
                while r < len(nums) and nums[r] == val:
                    r += 1
                if r < len(nums):
                    nums[l] = nums[r]
                    nums[r] = val
            l += 1
        return len(nums) - nums.count(val)

            