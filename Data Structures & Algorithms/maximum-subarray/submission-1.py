class Solution:
    """
    
    curr = 1
    num = 20

    
    """
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float("-inf")
        best = curr
        for num in nums:
            if num > curr and curr < 0:
                curr = num
            else:
                curr += num
            best = max(best, curr)
        return best