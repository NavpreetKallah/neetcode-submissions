class Solution:
    """
    
    digit = 3
    this maps to def

    first take d then move onto next digit

    then take e and move onto next digit

    once all of these numbers are processed stop
    
    """
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        combo = []

        def backtrack(i, j):
            if i >= len(digits):
                if combo:
                    res.append("".join(combo))
                return

            s = mapping[digits[i]]

            if j >= len(s):
                return
            
            combo.append(s[j])

            backtrack(i + 1, 0)

            combo.pop()

            backtrack(i, j + 1)

        backtrack(0, 0)

        return res

