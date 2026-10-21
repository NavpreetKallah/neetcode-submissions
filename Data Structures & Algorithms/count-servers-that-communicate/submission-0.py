class Solution:
    """
    
    2 servers in a row = 1
    3 servers in a row = 2 + 1
    4 servers in a row = 3 + 2 + 1
    
    """
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        communicating = set()

        for rowIdx, row in enumerate(grid):
            serversInRow = row.count(1)
            if serversInRow > 1:
                for colIdx, cell in enumerate(row):
                    if cell == 1:
                        communicating.add((rowIdx, colIdx))
        
        grid = list(map(list, zip(*grid)))

        print(grid)

        for colIdx, col in enumerate(grid):
            serversInCol = col.count(1)
            if serversInCol > 1:
                for rowIdx, cell in enumerate(col):
                    if cell == 1:
                        communicating.add((rowIdx, colIdx))

        return len(communicating)

        