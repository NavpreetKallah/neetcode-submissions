class Solution:
    """
    
    start from the start

    if the current letter is not in s1 set start and end to be 1 ahead and clear the count dict
    if it is in s1 increment count dict
    if s2counts is ever bigger than s1counts remove letters from start until it is equal again
    if at any point s1counts == s2counts we are done
    
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = 0
        found = False
        letterCount = 0
        s1counts = {}
        s2counts = {}
        for letter in s1:
            s1counts[letter] = s1counts.get(letter, 0) + 1

        while end < len(s2):
            letter = s2[end]

            if letter not in s1counts:
                end += 1
                start = end
                letterCount = 0
                s2counts = {}
            else:
                s2counts[letter] = s2counts.get(letter, 0) + 1
                letterCount += 1
                while s2counts[letter] > s1counts[letter]:
                    startLetter = s2[start]
                    s2counts[startLetter] -= 1
                    letterCount -= 1
                    start += 1
                    if s2counts[startLetter] == 0:
                        s2counts.pop(startLetter)
                end += 1

            if letterCount == len(s1):
                found = True
        



        return found