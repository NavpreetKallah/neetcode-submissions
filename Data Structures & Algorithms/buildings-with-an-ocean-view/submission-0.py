class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for idx, height in enumerate(heights):
            if stack:
                while stack and stack[-1][1] <= height:
                    stack.pop()

            stack.append((idx, height))
        return [element[0] for element in stack]
            