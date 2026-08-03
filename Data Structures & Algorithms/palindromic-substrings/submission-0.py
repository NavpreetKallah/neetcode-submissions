class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [0] * len(s)

        for i in range(len(s)):
            resIdx = 0
            resLen = 0
            l, r = i, i
            count1 = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count1 += 1
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            count2 = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count2 += 1
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            dp[i] += (dp[i - 1] if i != 0 else 0) + count1 + count2

        return dp[-1]