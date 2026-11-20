class Solution:
    def isUgly(self, n: int) -> bool:
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1