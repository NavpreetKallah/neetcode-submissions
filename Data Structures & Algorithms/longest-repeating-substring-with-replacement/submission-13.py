class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        longest = 0
        start = 0
        highestFreq = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            highestFreq = max(highestFreq, count[s[end]])

            while (end - start + 1) - highestFreq > k:
                count[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)


        return longest


