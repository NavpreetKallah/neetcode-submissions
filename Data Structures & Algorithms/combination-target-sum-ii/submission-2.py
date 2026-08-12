class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, currTarget):
            if currTarget == 0:
                res.append(subset.copy())
                return
            if currTarget < 0 or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i + 1, currTarget - candidates[i])

            subset.pop()

            skippedNum = candidates[i]
            curr = i
            while curr < len(candidates) - 1 and candidates[curr] == skippedNum:
                curr += 1
            if candidates[curr] != skippedNum:
                dfs(curr, currTarget)

        dfs(0, target)

        return res
