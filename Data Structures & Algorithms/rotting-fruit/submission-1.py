class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        R, C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = -1
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            minutes += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        return max(minutes, 0)
