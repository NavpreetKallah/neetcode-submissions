class Solution:
    def isValid(self, s: str) -> bool:
        openP = "[({"
        closeP = "])}"
        stack = []
        for letter in s:
            if letter in openP:
                stack.append(letter)
            else:
                if not stack:
                    return False
                indexP = closeP.index(letter)
                if stack[-1] != openP[indexP]:
                    return False
                else:
                    stack.pop(-1)
        return len(stack) == 0

               

        