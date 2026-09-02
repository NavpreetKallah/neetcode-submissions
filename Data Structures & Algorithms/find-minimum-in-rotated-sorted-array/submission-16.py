class Solution:
    """
    
    [6,1,2,3,4,5]

    l = 6
    r = 5
    mid = 3

    smallest is on left 

    l = 6
    r = 2
    mid = 1

    mid == smallest
    smallest on left


    [3,4,5,6,1,2]

    l = 3
    r = 2
    mid = 6

    smallest on right


    [4,5,6,7]

    l = 4
    r = 7

    """
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]
            