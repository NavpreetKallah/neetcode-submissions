class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        mid = 0
        while start <= end:
            mid = (end + start) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid + 1
            else:
                end = mid - 1
        if matrix[mid][0] > target:
            mid -= 1

        left = 0
        right = len(matrix[mid]) - 1

        while left <= right:
            rowMid = (left + right) // 2
            if matrix[mid][rowMid] == target:
                return True
            elif matrix[mid][rowMid] < target:
                left = rowMid + 1
            else:
                right = rowMid - 1

        return False
        
