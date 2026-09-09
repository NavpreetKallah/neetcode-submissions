class CountSquares:

    def __init__(self):
        self.points = {}
        self.biggest = 0

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        if p not in self.points:
            self.points[p] = 0
        self.points[p] += 1
        self.biggest = max(self.biggest, max(point))

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for i in range(-self.biggest, self.biggest):
            if i == 0:
                continue
            
            if (x + i, y) in self.points and (x + i, y + i) in self.points and (x, y + i) in self.points:
                res += self.points[(x + i, y)] * self.points[(x + i, y + i)] * self.points[(x, y + i)]
            if (x - i, y) in self.points and (x - i, y + i) in self.points and (x, y + i) in self.points:
                res += self.points[(x - i, y)] * self.points[(x - i, y + i)] * self.points[x, y + i]
        return res
