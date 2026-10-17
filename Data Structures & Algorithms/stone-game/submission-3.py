import functools

class Solution:
    """
    
    dfs(l, r, alice) = alice

    recursion relation
    max(dfs(l + 1, r, not alice) + piles[l], dfs(l, r - 1, not alice) + piles[r])
    
    """
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.cache
        def dfs(l, r):
            if l > r:
                return 0

            return max(dfs(l + 1, r) + piles[l], dfs(l, r - 1) + piles[r])
        
        return sum(piles) > sum(piles) // 2
