class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        minimum = 1
        maximum = 1
        tmax = float("-inf")
        for num in nums:
            xmax = maximum * num
            xmin = minimum * num
            minimum = min(xmax, xmin, num)
            maximum = max(xmax, xmin, num)
            tmax = max(tmax, minimum, maximum)

        return tmax

        



        