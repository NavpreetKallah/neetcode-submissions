class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def subsetFinder(num):
            tupleNum = tuple(num)
            if tupleNum in res:
                return
            res.add(tupleNum)
            for i in range(len(num)):
                subsetFinder(num[:i] + num[i + 1:])

        subsetFinder(nums)

        return [list(item) for item in res]

        


