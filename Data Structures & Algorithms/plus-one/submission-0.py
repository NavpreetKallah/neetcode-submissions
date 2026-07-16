class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newList = [-1] * len(digits)
        carry = 1
        for index, digit in enumerate(reversed(digits)):
            index = len(digits) - index - 1
            if digit == 9 and carry == 1:
                digit = 0
            else:
                digit += carry
                carry = 0
            newList[index] = digit
        if carry == 1:
            newList.insert(0, 1)
        return newList