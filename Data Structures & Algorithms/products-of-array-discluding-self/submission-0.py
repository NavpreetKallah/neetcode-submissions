import math
class Solution:
    start = [1,2,3,4]
    ans = [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 2 * 3]

    prefix = [1, 1, 1 * 2, 1 * 2 * 3]
    suffix = [1, 4, 4 * 3, 4 * 3 * 2]
    

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        prefix = [1]
        suffix = [1]
        for num in nums[:-1]:
            curr *= num
            prefix.append(curr)
        curr = 1
        for num in nums[::-1][:-1]:
            curr *= num
            suffix.insert(0, curr)
        return [prefix[i] * suffix[i] for i in range(len(nums))]
        

