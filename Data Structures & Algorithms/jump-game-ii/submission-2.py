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
        n = len(nums)
        if n == 1:
            return 0
        count = 0
        while r < n - 1:
            count += 1
            highest = r
            for i in range(l, r + 1):
                highest = max(highest, r + nums[i])
            l = r + 1
            r = highest
            print(l, r)
        return count