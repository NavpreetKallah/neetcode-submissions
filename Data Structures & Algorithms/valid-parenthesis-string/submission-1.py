class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []

        for idx, letter in enumerate(s):
            if letter == "(":
                leftStack.append(idx)
            elif letter == "*":
                starStack.append(idx)
            else:
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while leftStack:
            left = leftStack.pop()
            if not starStack:
                return False
            star = starStack.pop()

            if left > star:
                return False
        return True