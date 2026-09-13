'''

running max to keep track of largest islands

use dfs to traverse through islands
 - we still have a set but instead of just adding to it we also have a count
 - we pass count down recursively
 - when no tiles are left to be traversed we return count at that point


'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        rows,cols = len(grid), len(grid[0])
        count = [0]
        maxArea = 0

        def dfs(r,c):

            if r < 0 or c < 0 or r==rows or c==cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            count[0] += 1
        
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            
        
        for r in range(rows):
            for c in range(cols):
                count[0] = 0
                dfs(r,c)
                maxArea = max(maxArea,count[0])
        

        return maxArea
        