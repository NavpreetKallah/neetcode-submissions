class Solution:
    """

    [1, 3]

    [2, 3, 1]

    l = 2
    r = 1



    """
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        deflection = r

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        deflection = l
        l, r = 0, n - 1
        while l <= r:
            fakeMid = (l + r) // 2
            mid = (fakeMid + deflection) % n
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = fakeMid + 1
            else:
                r = fakeMid - 1
        return -1
        
            

