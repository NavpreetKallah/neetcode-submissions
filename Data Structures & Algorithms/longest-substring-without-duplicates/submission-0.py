class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()

        longest = 0

        start = 0
        end = 0
        while end < len(s):
            while s[end] in letters:
                letters.remove(s[start])
                start += 1

            letters.add(s[end])
            end += 1

            longest = max(end - start, longest)

        return longest


        
