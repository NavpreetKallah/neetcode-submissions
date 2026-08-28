class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        dp = {0}

        for num in nums:
            next = set(dp)
            for t in dp:
                if t + num == target:
                    return True
                elif t + num < target:
                    next.add(t + num)
            dp = next
        return False
        