from math import ceil
class Solution:
    """
    
    Can be optimised 

    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sumPiles = sum(piles)
        biggest = max(piles)
        lower = max(biggest // (h - len(piles) + 1), 1)
        upper = biggest + 1
                
        ans = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            
            if sumPiles / mid <= h:
                time = 0
                for pile in piles:
                    time += ceil(pile / mid)
                if time <= h:
                    ans = mid
                    upper = mid - 1
                else:
                    lower = mid + 1
            else:
                lower = mid + 1
        return ans
