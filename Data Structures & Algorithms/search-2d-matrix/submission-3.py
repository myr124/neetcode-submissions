'''
we have a grid and that is already sorted in non-decreasing order so its sorted
and we need to find a target

the twist here is that we have a grid but honestly the values are laid out
similar to a list but in the form of a matrix

so if we can flatten the matrix to represent a list then we have a solution

[0,0] [0,1] [0,2] [0,3]
[1,0] [1,1] [1,2] [1,3]
[2,0] [2,1] [2,2] [2,3]
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattenedList = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                flattenedList.append(matrix[r][c])
        
        l = 0
        r = len(flattenedList)-1

        while l<=r:
            m = l + ((r-l)//2)

            if flattenedList[m] > target:
                r = m-1
            elif flattenedList[m] < target:
                l = m+1
            else:
                return True
        
        return False
        