class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        curr_f = curr_s = 0
        res = []

        while curr_f < len(firstList) and firstList[curr_f] and curr_s < len(secondList) and secondList[curr_s]:
            start_f, end_f = firstList[curr_f]
            start_s, end_s = secondList[curr_s]

            start_i = max(start_f, start_s)
            end_i = min(end_f, end_s)

            if start_i <= end_i:
                res.append([start_i, end_i])

            if end_s > end_f:
                curr_f += 1
            elif end_s < end_f:
                curr_s += 1
            else:
                curr_f += 1
                curr_s += 1

        return res
            
