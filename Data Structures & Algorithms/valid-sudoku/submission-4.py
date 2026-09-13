class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # col 8 row 5
        # # col 9 row 4  - 7.333  - x: 3 y: 1.333
        # # col 9 row 5 -  8      - x: 3 y: 1.66
        # # col 9 row 6 -  9      - x: 3 y: 2
        # # col 9 row 8 
        # # 8/3
        # res = True
        # rows = set()
        # cols = set()
        # squares = {}
        # for r,k in enumerate(board):
        #     for c,l in enumerate(k):
        #         squares[tuple([r+1,c+1])] = set()
        # rowNum = 0
        # colNum = 0
        # for r,k in enumerate(board):
        #     rows= set()
        #     for c,l in enumerate(k):
        #         if l.isnumeric(): 
        #             if l in rows:
        #                 print("duplicate row")
        #                 res = False
        #             else:
        #                 rows.add(l)
        
        # while (rowNum < len(board) and colNum < len(board)):
        #     # print(board[rowNum][colNum])
        #     # print(rowNum)
        #     # print(colNum)
        #     if board[rowNum][colNum] in cols:
        #         print("duplicate col")
        #         res = False
        #     else:
        #         if board[rowNum][colNum].isnumeric():
        #             cols.add(board[rowNum][colNum])
        #         if rowNum==8:
        #             cols = set()
        #             if colNum<8:
        #                 colNum+=1
        #                 rowNum = 0
        #                 continue
        #             else:
        #                 break
        #         rowNum+=1
        # rowNum = 0
        # colNum = 0
        # for r,k in enumerate(board):
        #     for c,l in enumerate(k):
        #         if l.isnumeric():
        #             if l in squares[tuple([math.ceil((r+1)/3),math.ceil((c+1)/3)])]:
        #                 res = False
        #             else:
        #                 squares[tuple([math.ceil((r+1)/3),math.ceil((c+1)/3)])].add(l)


        # return res

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
        
        return True