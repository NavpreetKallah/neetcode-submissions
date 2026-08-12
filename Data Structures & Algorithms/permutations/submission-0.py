class Solution:
    """
    
    [1, 2, 3]

    
    2, 3

    1, 3
    
    1, 2
    
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)



        def helper(nums, output = []):
            for num in nums:
                helper([n for n in nums if n != num], output + [num])

            if len(output) == n:
                res.append(output)

        helper(nums)

        return res

            