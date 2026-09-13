"""
dfs
similar approach to number of isladns
but this time we also keep track of size of islands
I am thinking global variable to hold size of islands and we store max in
0th index of an array

return that value

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        islandsize = [0]
        res = 0
        visit = set()

        def dfs(r,c,visit):
            
            if min(r,c) < 0 or r==row or c==col or grid[r][c]==0 or (r,c) in visit:
                return
            
            print((r,c))
            if grid[r][c] == 1:
                islandsize[0]+=1
            
            visit.add((r,c))

            dfs(r+1,c,visit)
            dfs(r,c+1,visit)
            dfs(r-1,c,visit)
            dfs(r,c-1,visit)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r,c,visit)
                    res = max(islandsize[0],res)
                    islandsize[0] = 0
        

        return res

        


        