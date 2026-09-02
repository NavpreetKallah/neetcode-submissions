class Solution:
    """

    [1, 3]

    [2, 3, 1]

    l = 2
    r = 1



    """
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        new = nums[l:] + nums[:r]
        start = l
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if new[mid] == target:
                return (mid + start) % len(nums)
            elif new[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


