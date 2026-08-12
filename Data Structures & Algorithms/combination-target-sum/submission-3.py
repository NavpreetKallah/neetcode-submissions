class Solution:

    """
    
    try again ( go backwards its in the name )
    
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, currTarget):
            if currTarget == 0:
                res.append(subset.copy())
                return
            if currTarget < 0 or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, currTarget - nums[i])

            subset.pop()
            dfs(i + 1, currTarget)

        dfs(0, target)

        return res
