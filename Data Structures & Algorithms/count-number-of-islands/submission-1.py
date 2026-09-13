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

        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # Base: out of bounds or already visited or water
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            if grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r, c))
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)  # mark all connected land
        return islands

            








        