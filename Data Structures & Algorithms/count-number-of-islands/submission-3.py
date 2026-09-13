'''
2d grid where '1' represents land and '0' represents water count and return the number of islands


we use dfs to count an island, we put visited nodes in a visited set or mark it as '0' or any other boundary 

every time we start dfs we add one to our count

return count after everything is visited
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        rows, cols = len(grid), len(grid[0])
        numofislands = 0
        
        def dfs(r,c):
            if (r,c) in visited or r == rows or c == cols or c < 0 or r < 0 or grid[r][c] == "0":
                return
            
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    numofislands +=1
                    dfs(r,c)


        return numofislands
        