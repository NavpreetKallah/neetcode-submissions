class Solution:
    """
    
    [2,2,4]

    2, 2, 4, (2, 2)
    
    """
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        subset = []
        self.res = 0
        def backtrack(i):
            if i >= len(nums):
                return
            if nums[i] - k not in subset and nums[i] + k not in subset:
                self.res += 1
                subset.append(nums[i])
                backtrack(i + 1)
            try:
                subset.remove(nums[i])
            except:
                pass
            backtrack(i + 1)
        backtrack(0)
        return self.res