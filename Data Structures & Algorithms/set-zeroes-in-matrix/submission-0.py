'''

brute force would be to do grid traversal find zeroes then go through respective row and col and set everything to zero
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for j in range(0,cols):
                        if matrix[r][j]!= 0:
                            matrix[r][j] = "."
                    for k in range(0,rows):
                        if matrix[k][c]!= 0:
                            matrix[k][c] = "."

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == ".":
                    matrix[r][c] = 0
'''
matrix=[[1,2,3],
        [4,0,5],
        [6,7,8]]


'''
        