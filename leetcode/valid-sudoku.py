class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row validation
        for row in board:
            row_list = [x for x in row if x != "."]
            row_set = set(row_list)

            if len(row_list) > len(row_set):
                return False

        # Column validation
        for i in range(9):
            col_list = [row[i] for row in board if row[i] != "."]
            col_set = set(col_list)

            if len(col_list) > len(col_set):
                return False

        # Subgrid validation
        subgrids = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    subgrid_index = (i // 3) * 3 + (j // 3)
                    subgrids[subgrid_index].append(board[i][j])

        for subgrid in subgrids:
            if len(subgrid) > len(set(subgrid)):
                return False

        return True