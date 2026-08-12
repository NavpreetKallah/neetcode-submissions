class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, current_target):
            if current_target == 0:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or current_target < 0:
                return

            subset.append(nums[i])
            dfs(i, current_target - nums[i])

            subset.pop()
            dfs(i + 1, current_target)

        dfs(0, target)
        return res