class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(k):
            heapq.heappush_max(heap, (nums[i], i))

        for i in range(k - 1, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            best = heapq.heappop_max(heap)
            while best[1] <= i - k:
                best = heapq.heappop_max(heap)
            heapq.heappush_max(heap, best)
            res.append(best[0])

        return res
        