class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                        q.append((r,c))

        while q:
            r, c = q.popleft()
            board[r][c] = "E"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == "O":
                    q.append((nr, nc))
                    board[nr][nc] = "E"
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "E":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"



        