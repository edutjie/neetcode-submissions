class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rc in board:
            print(rc)
        col_counter = [[0] * 9 for _ in range(9)]
        box_counter = [[0] * 9 for _ in range(9)]
        for r in range(9):
            row_counter = [0] * 9
            for c in range(9):
                v = board[r][c]
                if v != ".":
                    v = int(v)
                    
                    # col check
                    row_counter[v-1] += 1
                    if row_counter[v-1] > 1:
                        return False

                    # row check
                    col_counter[c][v-1] += 1
                    if col_counter[c][v-1] > 1:
                        return False

                    # box check
                    box_idx = ((r//3) * 3) + (c//3)
                    box_counter[box_idx][v-1] += 1
                    if box_counter[box_idx][v-1] > 1:
                        return False
        return True
                