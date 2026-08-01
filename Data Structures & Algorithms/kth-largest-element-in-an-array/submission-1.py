class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minh = []

        for num in nums:
            if len(minh) < k:
                heapq.heappush(minh, num)
            else:
                if minh[0] < num:
                    heapq.heappushpop(minh, num)
        return minh[0]