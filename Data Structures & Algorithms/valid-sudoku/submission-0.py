class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(self.rowValid(board))
        print(self.colValid(board))
        print(self.boxValid(board))
        return self.rowValid(board) and self.colValid(board) and self.boxValid(board)

    def rowValid(self, board) -> bool:
        return all([self.validate(row) for row in board])

    def colValid(self, board) -> bool:
        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            if not self.validate(col):
                return False
        return True

    def boxValid(self, board) -> bool:
        boxWidth = range(len(board)//3)
        for i in boxWidth:
            for j in boxWidth:
                box = []
                for cell_x in boxWidth:
                    for cell_y in boxWidth:
                        box.append(board[i * 3 + cell_y][j * 3 + cell_x])
                if not self.validate(box):
                    return False
        return True

    def removeDots(self, array):
        return [element for element in array if element != "."]

    def validate(self, array):
        fixedArray = self.removeDots(array)
        return len(fixedArray) == len(set(fixedArray))
