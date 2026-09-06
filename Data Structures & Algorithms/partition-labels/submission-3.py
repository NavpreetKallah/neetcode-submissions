class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for idx, letter in enumerate(s):
            if letter not in pos:
                pos[letter] = [idx, idx]
            else:
                pos[letter][1] = idx
        
        print(pos)
        res = []
        for interval in pos.values():
            if res and interval[0] < res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        print(res)
        r = []
        for x, y in res:
            r.append(y - x + 1)
        return r
