class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r, c, ocean, old=0):
            if not 0 <= r < R or not 0 <= c < C:
                return 
            
            if (r, c) in ocean:
                return
            curr = heights[r][c]
            if curr >= old:
                ocean.add((r, c))

                for dr, dc in directions:
                    dfs(r + dr, c + dc, ocean, curr)

        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    dfs(r, c, pacific)

        for r in range(R):
            for c in range(C):
                if r == R - 1 or c == C - 1:
                    dfs(r, c, atlantic)

        return list(atlantic & pacific)

            