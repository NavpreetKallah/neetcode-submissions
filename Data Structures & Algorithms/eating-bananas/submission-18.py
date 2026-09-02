from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            timeTaken = sum(ceil(pile / mid) for pile in piles)
            if timeTaken <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res