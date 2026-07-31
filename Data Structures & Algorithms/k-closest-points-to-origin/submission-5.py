
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for idx, (x1, y1) in enumerate(points):
            dist = x1 ** 2 + y1 ** 2

            if len(maxheap) < k:
                heapq.heappush_max(maxheap, (dist, (x1, y1)))
            else:
                if dist < maxheap[0][0]:
                    heapq.heappushpop_max(maxheap, (dist, (x1, y1)))

        return [p for _, p in maxheap]