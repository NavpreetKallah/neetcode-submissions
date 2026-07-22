class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        area = 0
        while start < end:
            area = max((end - start) * min(heights[start], heights[end]), area)
            if heights[start] <= heights[end]:
                start += 1
            elif heights[start] >= heights[end]:
                end -= 1
            else:
                break
        return area