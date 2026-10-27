class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        print(counts)
        best = res = 0
        wearesoodd = 0
        for _, val in counts.items():
            if val % 2 == 1:
                res += val - 1
                wearesoodd = 1
            else:
                res += val
        res += best
        return res + wearesoodd