class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tCounts = {}
        for c in t:
            tCounts[c] = tCounts.get(c, 0) + 1

        count = 0
        sCounts = {}
        l = 0
        res = ""

        for r in range(len(s)):
            cr = s[r]
            sCounts[cr] = sCounts.get(cr, 0) + 1
            
            if cr in tCounts and sCounts[cr] == tCounts[cr]:
                count += 1

            while count == len(tCounts):
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r+1]
                
                cl = s[l]
                sCounts[cl] -= 1
                
                if cl in tCounts and sCounts[cl] < tCounts[cl]:
                    count -= 1
                
                l += 1

        return res