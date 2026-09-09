class Solution:
    """

    [3, 4]    
    [1, 2]

    7, 8, 9
    4, 5, 6
    1, 2, 3


    
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            temp = matrix[i]
            matrix[i] = matrix[n - 1 - i]
            matrix[n - 1 - i] = temp

        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

