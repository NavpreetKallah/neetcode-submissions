from functools import cache
class Solution:
    """
    
    Alice takes between 1 and 2M piles
    bob then takes between 1 and 4M piles

    dfs(i, M, alice) = alice

    alice = max(dfs(i+X, max(M,X)) + sum(piles[i:X]))
    bob = min((dfs(i+X, max(M,X)))
    
    """
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dfs(i, m, alice):
            if i >= len(piles):
                return 0
            best = 0 if alice else float("inf")
            for x in range(1, (2*m+1)):
                p = sum(piles[i:i+x])
                if alice:
                    best = max(best, dfs(i + x, max(x,m), not alice) + p)
                else:
                    best = min(best, dfs(i + x, max(x,m), not alice))
            return int(best)
        return dfs(0,1,True)
