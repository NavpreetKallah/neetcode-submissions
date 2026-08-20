class Solution:
    """
    
    try to make a word with letters
    once a word is made try to make a new word from that point

    at each of these have a split
    e.g if you never considered that word to exist

    
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = set()
        evilMemo = set()

        def dfs(i):
            if i == len(s):
                memo.add(i)
                return True

            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if j + 1 in evilMemo:
                        continue
                    if j + 1 in memo or dfs(j + 1):
                        return True
            evilMemo.add(i)
            return False

        return dfs(0)