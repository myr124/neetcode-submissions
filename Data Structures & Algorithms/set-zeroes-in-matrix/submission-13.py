'''

brute force would be to do grid traversal find zeroes then go through respective row and col and set everything to zero

how do we optimize iteration
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        rowMap = defaultdict(bool)
        colMap = defaultdict(bool)

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowMap[r] = True
                    colMap[c] = True
                    

        for r in range(rows):
            for c in range(cols):
                if rowMap[r] or colMap[c] == True:
                    matrix[r][c] = 0
'''
matrix=[[1,2,3],
        [4,0,5],
        [6,7,8]]


'''
        