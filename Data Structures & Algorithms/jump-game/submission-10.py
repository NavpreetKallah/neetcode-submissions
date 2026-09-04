class Solution:

    """
    
    [1,2,1,0,1]

    to get to the end we require atleast 1 at position 4
    if this is valid then we require atleast 1 at position 3
    and so forth

    if there is no 1 at position 4
    we then require atleast a 2 at position 3
    if this is not atleast 2 then we require atleast 3 at position 2
    
    """


    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        curr = 0
        for num in nums[::-1]:
            if num >= curr:
                curr = 1
            else:
                curr += 1
            
        return nums[0] >= curr