class Solution:

    """
    
    Detect Cycles
    if cycle return False 
    if not return True
    
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre = {}

        for c, p in prerequisites:
            if c not in courseToPre:
                courseToPre[c] = []
            courseToPre[c].append(p)

        visited = set()

        def dfs(pre):
            if pre in visited:
                return False

            if pre not in courseToPre:
                return True

            visited.add(pre)

            for p in courseToPre[pre]:
                if not dfs(p):
                    return False

            visited.discard(pre)
            del(courseToPre[pre])
            return True

        for c, p in prerequisites:
            if not dfs(p):
                return False

        return True