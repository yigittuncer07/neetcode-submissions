class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashsets = [set() for _ in range(len(board))]
        column_hashsets = [set() for _ in range(len(board))]
        grid_hashsets = [set() for _ in range(len(board))]

        for i, row in enumerate(board):
            row_hs = row_hashsets[i]
            for n, val in enumerate(row):
                if val == ".":
                    continue
                column_hs = column_hashsets[n]
                grid_hs = grid_hashsets[3 * math.floor(i / 3) + math.floor (n / 3)]
                if val in row_hs or val in column_hs or val in grid_hs:
                    return False
                row_hs.add(val)
                column_hs.add(val)
                grid_hs.add(val)
        return True
                