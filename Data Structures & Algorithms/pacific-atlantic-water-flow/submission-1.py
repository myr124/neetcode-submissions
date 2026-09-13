'''

heights[r][c]

represents the height above the sea level

water can flow in four directions

way to identify which ocean we start with


'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = []

        def bfs(r,c):
            pf = False
            af = False
            queue = deque([(r,c)])
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()

                if row == 0 or col == 0:
                    pf = True
                
                if row == rows-1 or col == cols-1:
                    af = True
                
                for dx,dy in directions:
                    rx = row + dx
                    cy = col + dy

                    if (rx,cy) in visited or rx <0 or cy < 0 or rx >= rows or cy>= cols or heights[rx][cy] > heights[row][col]:
                        continue
                    
                    queue.append((rx,cy))
                    visited.add((rx,cy))
            
            return af and pf

        for r in range(rows):
            for c in range(cols):
                visited = set()

                if bfs(r,c):
                    print((r,c))
                    print("True")
                    res.append([r,c])
        
        return res


                
