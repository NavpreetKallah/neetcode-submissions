class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= k + 1:
            return self.hasDuplicate(nums)

        for i in range(0, n - k):
            if self.hasDuplicate(nums[i:i+k+1]):
                return True
        return False     


    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) != len(nums))