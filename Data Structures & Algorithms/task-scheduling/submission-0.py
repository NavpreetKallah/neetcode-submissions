class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [(cnt, key) for key, cnt in count.items()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt, key = heapq.heappop_max(maxHeap)
                cnt -= 1
                if cnt:
                    q.append((cnt, time + n, key))
            if q and q[0][1] == time:
                cnt, time, key = q.popleft()
                heapq.heappush_max(maxHeap, (cnt, key))

        return time