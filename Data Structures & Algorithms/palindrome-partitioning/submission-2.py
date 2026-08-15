class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        validP = set()

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(i):
            if i == len(s):
                res.append(path.copy())
                return

            for end in range(i + 1, len(s) + 1):
                p = s[i:end]
                
                if p in validP or is_palindrome(p):
                    validP.add(p)
                    path.append(p)
                    backtrack(end)
                    path.pop()

        backtrack(0)

        return res