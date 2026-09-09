class CountSquares:
    def __init__(self):
        self.points = defaultdict(int)
        self.x_pts = defaultdict(list)

    def add(self, point: List[int]) -> None:
        px, py = point
        self.points[(px, py)] += 1
        self.x_pts[px].append(py)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for y1 in self.x_pts[x]:

            if y1 == y:
                continue

            d = abs(y1 - y)

            if (x + d, y) in self.points and (x + d, y1) in self.points:
                res += self.points[(x + d, y)] * self.points[(x + d, y1)]

            if (x - d, y) in self.points and (x - d, y1) in self.points:
                res += self.points[(x - d, y)] * self.points[(x - d, y1)]

        return res