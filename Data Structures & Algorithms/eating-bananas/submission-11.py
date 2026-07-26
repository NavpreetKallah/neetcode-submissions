from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sumPiles = sum(piles)
        biggest = max(piles)
        lower = max(biggest // (h - len(piles) + 1), 1)
        upper = biggest + 1
        for k in range(lower, upper):
            if sumPiles / k <= h:
                time = 0
                for pile in piles:
                    time += ceil(pile / k)
                if time <= h:
                    return k