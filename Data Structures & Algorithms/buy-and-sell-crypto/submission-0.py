class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = prices[0]
        for current in prices:
            if current < cheapest:
                cheapest = current
            profit = max(profit, current - cheapest)
        return profit