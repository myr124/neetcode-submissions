'''
you are given an m x n matrix board containing letters 'x' and 'o'


Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.


we iterate through outer ring of matrix

first pass we check for Os and then once we find it we do dfs on it and mark everything attached to it (set so we don't have to modify later)

then second pass we do floodfill or dfs from outer ring
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        circleset = set()
        rows,cols = len(board), len(board[0])

        def dfs(r,c):

            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "X" or (r,c) in circleset:
                return

            circleset.add((r,c))
            
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols - 1:
                    print("hallo")
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in circleset:
                    board[r][c] = "X"
        
        