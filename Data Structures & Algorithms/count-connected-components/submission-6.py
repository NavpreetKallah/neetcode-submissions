class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        res = 0
        visited = set()

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        print(adj)

        def dfs(prev, curr):
            if curr in visited:
                return
            visited.add(curr)
            for connection in adj[curr]:
                if connection == prev:
                    continue
                dfs(curr, connection)
                

        for i in range(n):
            if i not in visited and adj[i]:
                dfs(-1, i)
                res += 1
        return res + n - len(visited)
