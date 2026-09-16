class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hmap = {}
        coins.sort()

        def recurse(i, currAmount):
            if i >= len(coins):
                return 0

            if currAmount == 0:
                return 1

            if (i, currAmount) in hmap:
                return hmap[(i, currAmount)]

            
            res = recurse(i + 1, currAmount)         
            if currAmount - coins[i] >= 0:
                res += recurse(i, currAmount - coins[i])
            hmap[(i, currAmount)] = res
            return res

        return recurse(0, amount)

            