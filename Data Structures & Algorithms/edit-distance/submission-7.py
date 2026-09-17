class Solution:
    """
    
    monkeys
    money

    insert e into monkeys

    monekeys
    money

    +1 to w2i keep w1i the same
    
    """
    def minDistance(self, word1: str, word2: str) -> int:
        hmap = {}

        def recurse(w1i, w2i):
            if (w1i, w2i) in hmap:
                return hmap[(w1i, w2i)]
            if w1i == len(word1):
                return len(word2) - w2i
            if w2i == len(word2):
                return len(word1) - w1i

            res = float("inf")
            if word1[w1i] == word2[w2i]:
                res = recurse(w1i + 1, w2i + 1)
            
            res = min(res, recurse(w1i + 1, w2i + 1) + 1, recurse(w1i + 1, w2i) + 1, recurse(w1i, w2i + 1) + 1)
            hmap[(w1i, w2i)] = res
            return res

        return recurse(0, 0)