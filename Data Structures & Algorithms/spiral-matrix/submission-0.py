class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n = len(matrix) #rows
        m = len(matrix[0]) # cols

        i = 0
        j = 0
        count = 0

        while len(res) != n * m:

            while len(res) != n * m and j < m - count:
                res.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1

            while len(res) != n * m and i < n - count:
                res.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1

            while len(res) != n * m and j >= count:
                res.append(matrix[i][j])
                j -= 1

            j += 1
            i -= 1



            while len(res) != n * m and i >= count + 1:
                res.append(matrix[i][j])
                i -= 1

            i += 1
            j += 1

            count += 1

        return res