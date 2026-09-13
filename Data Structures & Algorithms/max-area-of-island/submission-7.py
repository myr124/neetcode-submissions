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

        rowLen , colLen = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        q = deque()

        count = 0

        def bfs(start_row,start_col):
            q = deque([[start_row, start_col]])
            visited.add((start_row, start_col))

            area = 0
            while q:
                row, col = q.popleft()
                area += 1
                

                for dr,dc in directions:
                    r = row + dr
                    c = col + dc 

                    if (r < 0 or c < 0 or r == rowLen or c == colLen or (r,c) in visited or grid[r][c] ==  0):
                        continue
                    
                    
                    visited.add((r,c))
                    q.append([r,c])
                    
                
            return area
        

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1 and (r,c) not in visited:
                    count = max(bfs(r,c), count)
        

        return count
            


            

