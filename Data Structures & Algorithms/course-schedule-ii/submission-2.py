class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[v].append(u)

        state = [0] * numCourses
        order = []
        def dfs(curr):
            if state[curr] == 1:
                return False
            if state[curr] == 2:
                return True
            state[curr] = 1
            valid = True
            for connection in adj[curr]:
                if not dfs(connection):
                    return False

            order.append(curr)
            state[curr] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0 and not dfs(i):
                return []
        return order[::-1]
            