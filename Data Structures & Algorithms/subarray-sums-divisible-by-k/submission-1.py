class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = [0] * k
        remainder_count[0] = 1
        
        running_sum = 0
        res = 0
        
        for num in nums:
            running_sum += num
            rem = running_sum % k
            
            res += remainder_count[rem]
            remainder_count[rem] += 1
            
        return res
