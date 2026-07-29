class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n
        while number != 1:
            if number in seen:
                return False

            seen.add(number)
            numList = []
            while number:
                digit = number % 10
                numList.append(digit)
                number //= 10
            summed = 0
            for num in numList:
                summed += int(num) ** 2
            number = summed
        return True