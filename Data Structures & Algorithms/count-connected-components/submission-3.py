class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        res = 0
        visited = set()
        existing = set()

        for start, end in edges:
            if start not in adj:
                adj[start] = []
            if end not in adj:
                adj[end] = []
            adj[start].append(end)
            adj[end].append(start)
            existing.add(start)
            existing.add(end)

        print(adj)

        def dfs(prev, curr):
            if curr in visited:
                return
            visited.add(curr)
            for connection in adj[curr]:
                if connection == prev:
                    continue
                dfs(curr, connection)
                

        for i in existing:
            if i not in visited:
                dfs(-1, i)
                res += 1
        return res + n - len(visited)
