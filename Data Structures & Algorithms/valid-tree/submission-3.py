class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        visited = set()

        if len(edges) != n - 1:
            return False

        if not edges:
            return True

        for start, end in edges:
            if start not in adj:
                adj[start] = []
            adj[start].append(end)
            if end not in adj:
                adj[end] = []
            adj[end].append(start)

        def dfs(prev, curr):
            if curr in visited:
                return False
            visited.add(curr)
            for edge in adj[curr]:
                if edge == prev:
                    continue
                if not dfs(curr, edge):
                    return False
            return True

        return dfs(-1, 0) and len(visited) == n
            