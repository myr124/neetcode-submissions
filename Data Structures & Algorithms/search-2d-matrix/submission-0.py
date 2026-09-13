class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 1
        R = (len(matrix) * len(matrix[0]))
        mid = (L + R) // 2
        while L <= R:
            col = (len(matrix[0]) - ((-(mid // -(len(matrix[0]))) * len(matrix[0])) - mid)) - 1
            row = -(mid // -(len(matrix[0]))) - 1
            # colLeft = (len(matrix[0]) - ((-(L // -(len(matrix[0]))) * len(matrix[0])) - L)) - 1
            # rowLeft = -(L // -(len(matrix[0]))) - 1
            # colRight = (len(matrix[0]) - ((-(R // -(len(matrix[0]))) * len(matrix[0])) - R)) - 1
            # rowRight = -(R // -(len(matrix[0]))) - 1

            if matrix[row][col] < target:
                L = mid+1
            elif matrix[row][col] > target:
                R = mid-1
            else:
                return True
            mid = (L+R)//2
            
        return False
        