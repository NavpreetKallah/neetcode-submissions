class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = {}
        dijkstras = {}
        for idx, manages in enumerate(manager):
            if manages not in tree:
                tree[manages] = []
            tree[manages].append(idx)
        
        for idx, time in enumerate(informTime):
            dijkstras[idx] = float("inf")

        dijkstras[headID] = 0
        q = deque([headID])

        while q:
            for _ in range(len(q)):
                item = q.popleft()
                for element in tree.get(item, []):
                    dijkstras[element] = min(dijkstras[item] + informTime[item], dijkstras[element])
                    q.append(element)
                    
        return max(dijkstras.values())

