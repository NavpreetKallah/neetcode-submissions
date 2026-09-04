class Solution:
    """
    
    I think we should keep running totals at all indicies of what would be needed to win

    start from the end 
    we then need 1 or more at the prior indicie 
    then we NEED 1 or more at the indicie before that but ideally we get 2 or more

    I am unsure how to count these
    
    """
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        count = 0
        while r < len(nums) - 1:
            count += 1
            change = max(nums[l:r + 1])
            l = r + 1
            r = r + change
        return count