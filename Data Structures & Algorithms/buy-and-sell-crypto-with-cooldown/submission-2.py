class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hmap = {}
        
        def recurse(i, own):
            if i >= len(prices):
                return 0
            
            if (i, own) in hmap:
                return hmap[(i, own)]
            
            if not own:
                #buying
                best = recurse(i + 1, True) - prices[i]
            else:
                #selling
                best = recurse(i + 2, False) + prices[i]
            
            #Do Nothing
            best = max(best, recurse(i + 1, own))
            hmap[(i, own)] = best
            return best
        
        return recurse(0, False)