class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hmap = {}
        def recurse(i, target):
            if target == 0 and i == len(nums):
                return 1
            if i == len(nums):
                return 0
            
            if (i, target) in hmap:
                return hmap[(i, target)]

            res = recurse(i + 1, target + nums[i]) + recurse(i + 1, target - nums[i])
            hmap[(i, target)] = res
            return res

        return recurse(0, target)