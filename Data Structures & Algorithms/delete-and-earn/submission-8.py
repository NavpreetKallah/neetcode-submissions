class Solution:
    """
    
    first find values that do not differ by 1 and take all of these
    what should be left is only numbers which have neighbours

    [1,2,2,3,3,3,4,4,6]

    [1,2,2,3,3,3,3,3,3,4,4]

    if we then group these into their total values when removed we can remove the lowest

    [(1,1), (2,4), (3,18), (4,8)]

    from this we can see taking 3 is better than taking 2 which removes 19 or 4 which removes 18


    
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        res = 0

        values = defaultdict(int)
        for num in nums:
            values[num] += num

        while len(values):
            min_lost = (float("inf"), 0)
            for num, value in values.items():
                lost = values.get(num + 1, 0) + values.get(num - 1, 0) - values[num]
                if min_lost[0] > lost:
                    min_lost = (lost, num)

            lost_num = min_lost[1]
            res += values.pop(lost_num, 0)
            values.pop(lost_num + 1, None)
            values.pop(lost_num - 1, None)

        return res


