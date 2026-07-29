class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        curr = 0
        answer = 0
        for num in nums:
            curr += num
            if (curr - k) in prefixSums:
                answer += prefixSums[(curr - k)]
            prefixSums[curr] = prefixSums.get(curr, 0) + 1
        return answer