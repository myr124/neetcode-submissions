'''

brute force would be to do grid traversal find zeroes then go through respective row and col and set everything to zero

how do we optimize iteration
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
                    

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for i in range(rows):
                print(matrix[i][0])
                matrix[i][0] = 0
        
        if rowZero:
            matrix[0] = [0]*cols
        


'''
matrix=[[1,2,3],
        [4,0,5],
        [6,7,8]]

        [[0,0,0,0],
         [3,4,5,0],
         [0,3,1,0]]

         [[0,0,0,0,0],
         [0,0,0,0,0],
         [2147483647,2,-9,-6,0]]

        [[-4,-2147483648,6,-7,0],
         [-8,6,-8,-6,0],
         [2147483647,2,-9,-6,-10]]

'''
        