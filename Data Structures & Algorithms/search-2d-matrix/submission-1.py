class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        L = 1
        R = num_rows * num_cols
        
        while L <= R:
            mid = (L + R) // 2
            row = (mid - 1) // num_cols
            col = (mid - 1) % num_cols

            if matrix[row][col] < target:
                L = mid + 1
            elif matrix[row][col] > target:
                R = mid - 1
            else:
                return True
        
        return False