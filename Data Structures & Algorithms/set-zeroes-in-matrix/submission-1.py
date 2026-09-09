class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        zr = set()
        zc = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zr.add(i)
                    zc.add(j)

        for i in range(n):
            for j in range(m):
                if i in zr or j in zc:
                    matrix[i][j] = 0