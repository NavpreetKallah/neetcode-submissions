class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            curr = i
            oldNum = nums[i]
            while curr < len(nums) and nums[curr] == oldNum:
                curr += 1
            backtrack(curr)

        backtrack(0)

        return res