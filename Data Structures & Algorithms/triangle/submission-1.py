class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        self.hmap = {}

        def backtracking(row, i):
            if row >= n:
                return 0
            
            if (row, i) in self.hmap:
                return self.hmap[(row, i)]

            res = min(backtracking(row + 1, i), backtracking(row + 1, i + 1)) + triangle[row][i]
            self.hmap[(row, i)] = res

            return res



        return backtracking(0, 0)