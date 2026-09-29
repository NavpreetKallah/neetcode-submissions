class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = Counter(nums)
        return n.most_common()[0][0]