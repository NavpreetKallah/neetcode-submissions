class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answerDict = {}
        for index, num in enumerate(numbers, start=1):
            if num in answerDict:
                return [answerDict[num], index]
            answerDict[target - num] = index
