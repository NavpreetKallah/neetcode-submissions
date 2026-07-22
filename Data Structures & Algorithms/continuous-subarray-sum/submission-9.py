class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        curr = 0
        
        for index, num in enumerate(nums):
            curr += num
            remainder = curr % k
            
            if remainder in seen:
                if index - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = index
                
        return False