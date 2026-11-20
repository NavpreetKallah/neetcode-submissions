class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for start, end, distance in roads:
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []
            graph[start].append((end, distance))
            graph[end].append((start, distance))
        
        dijkstra = {i + 1: float("inf") for i in range(n)}
        dijkstra[1] = 0
        visited = set()
        
        q = deque([1])

        while q:
            n = len(q)
            for _ in range(n):
                start = q.popleft()
                for neighbour, distance in graph[start]:
                    if neighbour in visited:
                        continue
                    dijkstra[neighbour] = min(dijkstra[neighbour], distance)
                    q.append(neighbour)
                visited.add(start)
        dijkstra[1] = float("inf")
        return min(dijkstra.values())