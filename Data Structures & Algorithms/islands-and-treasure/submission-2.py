class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visit = set()
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        length = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                if grid[r][c] == 2147483647:
                    grid[r][c] = length
                
                neighbors = [[0,1],[1,0],[-1,0],[0,-1]]

                for dr,dc in neighbors:
                    if min(r+dr,c+dc) < 0 or r+dr ==row or c+dc == col or (r+dr,c+dc) in visit or grid[r+dr][c+dc]!=2147483647:
                        continue
                    q.append((r+dr,c+dc))
                    visit.add((r+dr, c+dc))
            
            length+=1
    

            
