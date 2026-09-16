class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hmap = {}
        def recurse(t1i, t2i):
            if t1i >= len(text1) or t2i >= len(text2):
                return 0

            if (t1i, t2i) in hmap:
                return hmap[(t1i, t2i)]

            if text1[t1i] == text2[t2i]:
                return recurse(t1i + 1, t2i + 1) + 1
            
            best = max(recurse(t1i + 1, t2i), recurse(t1i, t2i + 1))
            hmap[(t1i, t2i)] = best
            return best
        
        return recurse(0, 0)