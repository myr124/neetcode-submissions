class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visit = set()
        ROW = len(image)
        COL = len(image[0])
        startcolor = image[sr][sc]
        res = image

        def dfs(grid, r,c, visit):
            if min(r,c)<0 or r==ROW or c == COL or (r,c)in visit or grid[r][c] != startcolor:
                return
            
            if grid[r][c] == startcolor:
                grid[r][c] = color
            
            visit.add((r,c))
            
            dfs(grid, r+1,c,visit)
            dfs(grid, r,c+1,visit)
            dfs(grid, r-1,c,visit)
            dfs(grid, r,c-1,visit)

            visit.remove((r,c))

        dfs(res,sr,sc,visit)

        return res
        
            
            
        