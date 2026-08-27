class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        res = 0
        visited = set()

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for connection in adj[curr]:
                dfs(connection)
                

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
