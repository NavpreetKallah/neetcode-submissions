class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        colSize = len(grid)
        rowSize = len(grid[0])
        islands = set()
        count = 0

        def dfs(row, col):
            if not 0 <= col < rowSize or not 0 <= row < colSize or (row, col) in islands:
                return
            if grid[row][col] == "0":
                return
            islands.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            

        for rowIdx, row in enumerate(grid):
            for colIdx, cell in enumerate(row):
                if (rowIdx, colIdx) in islands or cell == "0":
                    continue
                count += 1
                dfs(rowIdx, colIdx)

        return count
