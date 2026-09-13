"""
-edges cases
- out of bounds (over and underflow)
- in visit
- if 1
- 
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0,1))
        visit.add((0,0))

        if grid[0][0] == 1:
            return -1

        def bfs(grid):
            while queue:
                r, c,length = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]

                for dr,dc in neighbors:
                    if (min(r+dr,c+dc)<0 or r+dr==ROWS or c+dc ==COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc]==1):
                        continue
                  
                    queue.append((r+dr,c+dc,length+1))
                    visit.add((r+dr,c+dc))
                print(queue)
                length+=1
        
        res = bfs(grid)

        return res if res is not None else -1


"""
[0,1]
[1,0] 
"""

        