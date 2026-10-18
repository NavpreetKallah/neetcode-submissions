
import functools

class Solution:
    """
    
    dfs(l, r) = alice

    recursion relation
    max(dfs(l + 1, r) + piles[l], dfs(l, r - 1) + piles[r])
    
    """
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.cache
        def dfs(l, r):
            if l > r:
                return 0

            return True
        return dfs(0, len(piles) - 1)