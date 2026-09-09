class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0] * (len(num1) + len(num2))

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                answer = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += answer
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] %= 10



        curr = len(res) - 1
        while curr >= 0 and res[curr] == 0:
            curr -= 1
        if curr == -1:
            return "0"
        return "".join(map(str,res[curr::-1]))