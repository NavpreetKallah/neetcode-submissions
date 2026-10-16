class Solution:
    """
    
    dfs(l, r, alice) = (alice, bob)

    recursion relation
    max(dfs(l + 1, r, not alice) + piles[l], dfs(l, r - 1, not alice) + piles[r])
    
    """
    def stoneGame(self, piles: List[int]) -> bool:
        
        hmap = {}
        def dfs(l, r, alice):
            if l > r:
                return 0
            if (l, r, alice) in hmap:
                return hmap[(l, r, alice)]
            best = max(dfs(l + 1, r, not alice) + piles[l], dfs(l, r - 1, not alice) + piles[r])
            hmap[(l, r, alice)] = best
            return best
        
        return dfs(0, len(piles) - 1, True) > sum(piles) // 2