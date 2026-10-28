class Solution:
    def largestOddNumber(self, num: str) -> str:
        curr = len(num) - 1
        while curr >= 0 and self.isEven(num[curr]):
            curr -= 1
        return num[:curr+1]

    def isEven(self, letter):
        if letter in "02468":
            return True
        return False
