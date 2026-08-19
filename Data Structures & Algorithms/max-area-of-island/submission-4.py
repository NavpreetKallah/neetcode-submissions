class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowNum = len(grid)
        colNum = len(grid[0])

        maximum = 0
        visited = set()

        def dfs(r, c):
            if not 0 <= r < rowNum or not 0 <= c < colNum:
                return 0

            if grid[r][c] != 1:
                return 0

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            

        for r in range(rowNum):
            for c in range(colNum):
                maximum = max(maximum, dfs(r, c))

        return maximum