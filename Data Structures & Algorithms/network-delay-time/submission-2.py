class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for source, destination, time in times:
            edges[source].append((destination, time))

        heap = [(0, k)]
        visited = set()
        t = 0

        while heap:
            time, source = heapq.heappop(heap)
            if source in visited:
                continue
            visited.add(source)

            t = time

            for destination, time2 in edges[source]:
                if destination in visited:
                    continue
                heapq.heappush(heap, (time + time2, destination))

        return t if len(visited) == n else -1



