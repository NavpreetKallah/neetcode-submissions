class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answerDict = {}
        for index, num in enumerate(numbers):
            if num in answerDict:
                return [answerDict[num], index + 1]
            answerDict[target - num] = index + 1
