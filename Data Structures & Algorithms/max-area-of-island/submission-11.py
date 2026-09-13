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
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rowlen,collen = len(grid), len(grid[0])
        maxarea = 0

        def bfs(start_row, start_col):
            
            queue = deque()
            queue.append((start_row, start_col))
            visited.add((start_row, start_col))
            area = 0

            while queue:
                row, col = queue.popleft()
                area += 1
                

                for dr,dc in directions:
                    r = row+dr
                    c = col+dc

                    if r >= rowlen or c >= collen or grid[r][c] == 0 or r < 0 or c < 0 or (r,c) in visited:
                        continue
                    
                    visited.add((r,c))
                    queue.append((r,c))
                
            return area

        for row in range(rowlen):
            for col in range(collen):
                if grid[row][col] == 1 and (row,col) not in visited:
                    
                    maxarea = max(bfs(row,col),maxarea)    

            

        return maxarea

            
            


            

