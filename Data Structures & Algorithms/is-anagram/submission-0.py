class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in set(s + t):
            if s.count(letter) != t.count(letter):
                return False
        return True