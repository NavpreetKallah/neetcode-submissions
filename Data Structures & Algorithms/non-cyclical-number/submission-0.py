class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        curr = n
        while curr != 1:
            if curr in seen:
                return False
            seen.append(curr)
            curr = self.helper(curr)
        return True

    def helper(self, n):
        return sum(map(lambda x: x * x, map(int, str(n))))