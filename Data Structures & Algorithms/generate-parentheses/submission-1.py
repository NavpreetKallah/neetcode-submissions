class Solution:

    """
    
    backtrack(0, 1)

    if close == 0:
        string += "("
        backtrack(close + 1, left - 1)
        string.pop()

    if close == 1:
        string += ")"
        backtrack(close - 1, left)
        string.pop()
    
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []

        def backtrack(close, left):
            if left == 0 and close == 0:
                res.append("".join(string))
                return
            
            if left > 0:
                string.append("(")
                backtrack(close + 1, left - 1)
                string.pop()
            if 0 < close <= n:
                string.append(")")
                backtrack(close - 1, left)
                string.pop()
            

        backtrack(0, n)

        return res