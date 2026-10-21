class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1), len(word2)
        length = max(n, m)
        res = "".join(
            (word1[i] if i < n else "") + 
            (word2[i] if i < m else "")
            for i in range(length)
        )
        return res