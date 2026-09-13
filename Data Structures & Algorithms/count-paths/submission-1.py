'''
basic 2d dp question

we can do basic dfs approach and optimize with memoization
then we can do bottom-up solution
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # brute force approach
        '''
        def dfs(r,c, rows, cols):
            if r == rows or c == cols:
                return 0
            if r == rows - 1 and c == cols-1:
                return 1

            return (dfs(r+1,c,rows,cols) + dfs(r,c+1,rows,cols))
        
        print(dfs(0,0,m,n))

        return dfs(0,0,m,n)
        '''
        
        # memoization (top-down approach)

        def memoization(r,c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = (memoization(r+1,c,rows,cols,cache)+memoization(r,c+1,rows,cols,cache))
            return cache[r][c]
        
        return memoization(0,0,m,n,[[0]*n for i in range(m)])

        