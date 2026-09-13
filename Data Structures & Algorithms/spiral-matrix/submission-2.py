class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """


        rows,cols = len(matrix), len(matrix[0])

        x,y,dy,dx = 0,0,0,1

        visited = set()

        res = []

        '''
        dy = dx
        dx = -dy
        '''

        for _ in range(rows*cols):
            print((y,x))
            res.append(matrix[y][x])
            visited.add((y,x))

            if (y+dy,x+dx) in visited or x+dx == cols or x+dx < 0 or y+dy == rows or y+dy < 0:
                temp = dy
                dy = dx
                dx = temp*-1

            x += dx
            y += dy
            
        return res      
        

        