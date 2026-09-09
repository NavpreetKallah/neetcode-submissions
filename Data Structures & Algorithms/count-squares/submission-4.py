class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        if p not in self.points:
            self.points[p] = 0
        self.points[p] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for x1, y1 in self.points.keys():
            if x1 == x:
                d = abs(y1 - y)

                if d == 0:
                    continue

                if (x + d, y) in self.points and (x1 + d, y1) in self.points:
                    res += self.points[(x + d, y)] * self.points[(x1 + d, y1)] * self.points[(x1, y1)]
                if (x - d, y) in self.points and (x1 - d, y1) in self.points:
                    res += self.points[(x - d, y)] * self.points[(x1 - d, y1)] * self.points[(x1, y1)]
        return res
                
