class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rc in board:
            print(rc)
        row_counter = [[0] * 9 for _ in range(9)]
        # col_counter = [0] * 9
        box_counter = [[0] * 9 for _ in range(9)]
        for r in range(9):
            col_counter = [0] * 9
            for c in range(9):
                v = board[r][c]
                if v != ".":
                    v = int(v)
                    
                    # col check
                    col_counter[v-1] += 1
                    if col_counter[v-1] > 1:
                        # print(r, c)
                        # print(v)
                        # print(col_counter)
                        return False

                    # row check
                    row_counter[c][v-1] += 1
                    if row_counter[c][v-1] > 1:
                        # print(r, c)
                        # print(v)
                        # for rc in row_counter:
                        #     print(rc)
                        return False

                    box_idx = ((r//3) * 3) + (c//3)
                    box_counter[box_idx][v-1] += 1
                    if box_counter[box_idx][v-1] > 1:
                        return False
        return True
                