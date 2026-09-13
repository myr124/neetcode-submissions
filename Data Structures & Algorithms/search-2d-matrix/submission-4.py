'''
You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.
   l
   0  1  2  3
[0[1, 2, 4, 8],
  [10,11,12,13],
 2[14,20,30,40]]
            r

[0][0]= 8
[2][3] = 40
[1][1]

[[1, 2, 4, 8], [10,11,12,13], [14,20,30,40]]

l = 0
len(matrix) * len(matrix[0]) - 1
r = rows*cols - 1

while l<=r
    m = (l+r)//2
    
    5 // 4  = 1

    5 % 4 = 1

    row = m // cols
    cols = m % cols


n values in an array

o(log m*n)
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0, (len(matrix) * len(matrix[0]))-1

        while l <=r:
            m = (l+r) // 2
            row = m // cols
            col = m % cols

            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        
        return False
        