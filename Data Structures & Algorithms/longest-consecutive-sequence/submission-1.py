class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        starts = []
        for num in numsSet:
            if num - 1 not in numsSet:
                starts.append(num)
        longest = 0
        for start in starts:
            length = 1
            curr = start
            while curr + 1 in numsSet:
                curr += 1
                length += 1
            longest = max(longest, length)
        return longest