class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for index, num in enumerate(nums):
            if num in targets.keys():
                return [targets[num], index]
            targets[target - num] = index
            
