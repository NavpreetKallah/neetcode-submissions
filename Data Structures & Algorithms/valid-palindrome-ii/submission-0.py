class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            skipLeft = s[l+1:r+1]
            skipRight = s[l:r]
            return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
        return True

