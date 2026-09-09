class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1R = num1[::-1]
        num2R = num2[::-1]

        res = 0
        for botIdx, bot in enumerate(num2R):
            for topIdx, top in enumerate(num1R):
                res += int(top) * int(bot) * (10 ** botIdx) * (10 ** topIdx)
        return str(res)