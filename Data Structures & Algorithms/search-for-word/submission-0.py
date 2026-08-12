class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowSize = len(board[0])
        colSize = len(board)
        letters = set(word)
        valid = False

        def dfs(r, c, curr=0):
            if curr == len(word):
                return True
                
            if not 0 <= r < colSize or not 0 <= c < rowSize or board[r][c] != word[curr]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (dfs(r, c + 1, curr + 1) or
                     dfs(r, c - 1, curr + 1) or
                     dfs(r + 1, c, curr + 1) or
                     dfs(r - 1, c, curr + 1))

            board[r][c] = temp

            return found
            
        for row in range(colSize):
            for col in range(rowSize):
                if dfs(row, col):
                    return True
        return valid


        