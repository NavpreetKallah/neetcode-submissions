class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = [0] * len(height)
        currMax = 0
        for h in height:
            currMax = max(h, currMax)
            leftMax.append(currMax)
        currMax = 0
        for i in range(len(height) - 1, -1, -1):
            currMax = max(height[i], currMax)
            rightMax[i] = currMax

        res = 0
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

