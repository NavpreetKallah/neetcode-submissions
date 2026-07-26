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
        smallest = nums[r]
        while l < r:
            print(l, r)
            mid = (l + r) // 2
            print(mid)

            if nums[l] < nums[mid] and nums[mid] < nums[r]:
                r = mid - 1
            elif nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1

            smallest = min(smallest, nums[mid])
        
        mid = (l + r) // 2
        smallest = min(smallest, nums[mid])

        return smallest