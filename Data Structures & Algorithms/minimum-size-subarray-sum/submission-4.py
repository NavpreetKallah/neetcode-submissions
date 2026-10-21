class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, res = 0, float("inf")
        l = r = 0
        n = len(nums)

        for r in range(n):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return res if res != float("inf") else 0