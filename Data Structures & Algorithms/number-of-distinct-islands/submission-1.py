'''
matrix traversal question
similar to number of islands
but we keep it distinct

An island is considered to be the same as another if and only if one island can be translated 
(and not rotated or reflected) to equal the other.

matrix dfs to find islands


(0,0) (0,1)         (2,3) (2,4)
(1,0) (1,1)         (3,3) (3,4)

we take the changes calculate recursively compare with previous islands store by size and have differences
'''


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        row = len(grid)
        print(row)
        col = len(grid[0])
        visit = set()
        uniqueislands = set()

        def dfs(r,c,d):
            if min(r,c) < 0 or r >= len(grid) or c >=len(grid[0]) or (r,c) in visit or grid[r][c] == 0:
                return
            
            visit.add((r,c))
            directions.append(d)
            

            dfs(r-1,c,"d")
            dfs(r+1,c,"u")
            dfs(r,c+1,"r")
            dfs(r,c-1,"l")
            directions.append("0")

        print(uniqueislands)

        for r in range(row):
            for c in range(col):
                directions = []
                dfs(r,c,"0")
                if directions:
                    uniqueislands.add(tuple(directions))

        print(uniqueislands)
        
        return len(uniqueislands)

            

            
            
        