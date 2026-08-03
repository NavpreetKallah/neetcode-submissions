class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0

        for i in range(len(s)):
            l, r = i, i
            count1 = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count1 += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            count2 = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count2 += 1
                l -= 1
                r += 1

            totalCount += count1 + count2

        return totalCount