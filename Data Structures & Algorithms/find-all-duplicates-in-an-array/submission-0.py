class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        values = set()
        res = []
        for num in nums:
            if num in values:
                res.append(num)
            values.add(num)
        return res


