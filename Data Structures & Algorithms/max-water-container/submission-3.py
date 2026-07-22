class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        area = 0
        while start < end:
            area = max((end - start) * min(heights[start], heights[end]), area)
            print(heights[start], heights[end])
            if heights[start] < heights[start+1] or heights[start] <= heights[end]:
                start += 1
            elif heights[end] < heights[end-1] or heights[start] >= heights[end]:
                end -= 1
            else:
                break
        return area