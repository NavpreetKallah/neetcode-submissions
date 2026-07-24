class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                oldIndex = stack.pop(-1)
                res[oldIndex] = (index - oldIndex)
            stack.append(index)
            
        return res

