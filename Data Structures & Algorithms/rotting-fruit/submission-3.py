class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        R, C = len(grid), len(grid[0])
        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        while q and fresh > 0:
            size = len(q)
            minutes += 1
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return minutes if fresh == 0 else -1
