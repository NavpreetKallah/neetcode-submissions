class Solution:

    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)

        if len(nums) == 1:
            return nums[0]

        for idx, num in enumerate(nums[1:]):
            dp1[idx] = max(dp1[idx - 2] if idx - 2 >= 0 else 0
                        , dp1[idx - 3] if idx - 3 >= 0 else 0) + num

        for idx, num in enumerate(nums[:-1]):
            dp2[idx] = max(dp2[idx - 2] if idx - 2 >= 0 else 0
                        , dp2[idx - 3] if idx - 3 >= 0 else 0) + num

        return max(max(dp1), max(dp2))

        