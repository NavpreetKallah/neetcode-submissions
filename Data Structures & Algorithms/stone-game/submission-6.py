import functools

class Solution:
    """
    
    dfs(l, r, alice) = diff

    recursion relation
    max(dfs(l + 1, r, not alice) + piles[l], dfs(l, r - 1, not alice) + piles[r])
    
    """
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.cache
        def dfs(l, r, alice):
            if l > r:
                return 0
            left = piles[l] if alice else 0
            right = piles[r] if alice else 0

            return max(dfs(l + 1, r, not alice) + left, dfs(l, r - 1, not alice) + right)
        
        return dfs(0, len(piles) - 1, True) > sum(piles) // 2