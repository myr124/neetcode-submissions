class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        row = len(grid)
        col = len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))

        # instead of calling bfs helper just do a multi source bfs

        while q:
            r, c = q.popleft()
            
            neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == row or nc < 0 or nc == col or grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))