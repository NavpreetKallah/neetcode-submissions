class Solution:
    def isPalindrome(self, s: str) -> bool:
        betterS = [c.lower() for c in s if c.isalnum()]
        return betterS == betterS[::-1]
        