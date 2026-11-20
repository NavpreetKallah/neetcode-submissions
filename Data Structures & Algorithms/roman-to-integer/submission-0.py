class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        pre = {
            "I": "",
            "V": "I",
            "X": "I",
            "L": "X",
            "C": "X",
            "D": "C",
            "M": "C"
        }

        ordering = "IVXLCDM"

        curr = 0
        res = 0
        while curr < len(s):
            count = 1
            token = s[curr]
            curr += 1
            while curr < len(s) and s[curr] == token:
                count += 1
                curr += 1
            if curr < len(s) and pre[s[curr]] == token:
                res -= count * symbols[token]
            else:
                res += count * symbols[token]
        
        return res
