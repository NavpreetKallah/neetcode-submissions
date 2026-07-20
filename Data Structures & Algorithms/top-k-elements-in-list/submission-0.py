class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(0,len(nums) + 1)]
        counts = {}
        res = []
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        for key, value in counts.items():
            freqs[value].append(key)
        for freq in freqs[::-1]:
            res += freq
        return res[:k]
        