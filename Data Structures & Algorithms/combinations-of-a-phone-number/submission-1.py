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

        def backtrack(i):
            if i >= len(digits):
                if combo:
                    res.append("".join(combo))
                return

            s = mapping[digits[i]]

            for c in s:
            
                combo.append(c)

                backtrack(i + 1)

                combo.pop()

        backtrack(0)

        return res

