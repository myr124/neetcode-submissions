class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        visit = set()
        ROW = len(grid)
        COL = len(grid[0])


        def dfs(r,c,visit):
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visit or grid[r][c] == 1:
                return 0
            

            if r == ROW-1 and c == COL-1:
                return 1
            
            visit.add((r,c))
            
            count = 0
            count += dfs(r+1,c,visit)
            count += dfs(r,c+1,visit)
            count += dfs(r-1,c,visit)
            count += dfs(r,c-1,visit)
            
            visit.remove((r,c))

            return count

        res = dfs(0,0,visit)

        return res
            
            

        