class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # hashset [1-9] - the keys would be rows

        # 0: [1,2,3]

        # rows [1-9] = {1:set()}
        # cols [1-9]
        # subgrid [1-9]



        # board[0][1]
        # nested for loop through whole matrix


        # row[r]
        # col[c]
        # subgrid[(r//3,c//3)]

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True
                