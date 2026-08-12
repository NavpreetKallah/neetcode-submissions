class Solution:
    """
    
    inefficient
    
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)

        def backtrack(start):

            if start == n:
                res.append(nums[:])

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]

                backtrack(start + 1)

                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)

        return res

            