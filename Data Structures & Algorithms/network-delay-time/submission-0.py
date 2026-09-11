class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))

        heap = [(0, k)]
        visited = set()
        t = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = time

            for node2, time2 in edges[node]:
                if node2 not in visited:
                    heapq.heappush(heap, (time + time2, node2))
        return t if len(visited) == n else -1




