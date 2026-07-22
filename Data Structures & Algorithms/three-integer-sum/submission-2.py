class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answerDict = {}
        for num1Index, num1 in enumerate(nums):
            for num2Index, num2 in enumerate(nums):
                if num1Index == num2Index:
                    continue
                total = -(num1 + num2)
                if total not in answerDict:
                    answerDict[total] = []
                answerDict[total].append([(num1Index, num1), (num2Index, num2)])
        
        answers = set()
        for index, num in enumerate(nums):
            if num in answerDict:
                existingNums = answerDict[num]
                for existingNum in existingNums:
                    indexs, numbers = zip(*existingNum)
                    numbers = list(numbers)
                    if index not in indexs:
                        numbers.append(num)
                        numbers.sort()
                        answers.add(tuple(numbers))

        
        return list(answers)