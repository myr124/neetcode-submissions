"""
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

1. visit array is important
2. we have a set so o(1) lookups
3. when we add 1s maybe instead of just adding (r,c) to set we can add (1,r,c)
4. this way we can distinguish 1s and 0s and see if adjacent land exists for the node we're currently in
5. what adjacency helps with is determining if the island is unique

code

dfs trav
base condition
    - out of bounds(over and under)
    - in visited

    visit.add((r,c))
    
    count += dfs()
    count += dfs()
    count += dfs()
    count += dfs()
    
    visit.remove((r,c))

    if node.val == 1:
        check if adjacent spots have ones and were visited:
        if false:
            return 1
        if true 
    
    
    
    

"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visit = set()
        row = len(grid)
        col = len(grid[0])
        
        def dfs(r,c,visit):

            if min(r,c) < 0 or r == row or c == col or grid[r][c] == "0" or (r,c) in visit:
                return
            
            visit.add((r,c))

            dfs(r+1,c,visit)
            dfs(r,c+1,visit)
            dfs(r-1,c,visit)
            dfs(r,c-1,visit)



        islands = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands+=1
                    dfs(r,c,visit)
        
        return islands
                    
            








        