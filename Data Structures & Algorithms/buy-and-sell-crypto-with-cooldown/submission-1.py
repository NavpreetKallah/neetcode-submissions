class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hmap = {}
        
        def recurse(i, own, current):
            if i >= len(prices):
                return current
            
            if (i, own, current) in hmap:
                return hmap[(i, own, current)]
            
            if not own:
                #buying
                best = recurse(i + 1, True, current - prices[i])
            else:
                #selling
                best = recurse(i + 2, False, current + prices[i])
            
            #Do Nothing
            best = max(best, recurse(i + 1, own, current))
            hmap[(i, own, current)] = best
            return best
        
        return recurse(0, False, 0)