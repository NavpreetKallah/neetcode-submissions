
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        res = []

        for idx, (x1, y1) in enumerate(points):
            heapq.heappush(maxheap, (((x1) ** 2 + (y1) ** 2), idx))

        for _ in range(k):
            item, idx = heapq.heappop(maxheap)
            res.append(points[idx])

        return res