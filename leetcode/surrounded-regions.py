class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find all O's on the edges , dfs to all other O's
        #save those coords and replace everything else with x's
        seen = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col):
            if ((row,col) in seen or 
                row < 0 or row == rows or
                col < 0 or col == cols or
                board[row][col]!="O" ):
                return
            seen.add((row,col))
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for row in range(rows):
            if(board[row][0] =="O"):#firs collunmn
                dfs(row,0)
            if(board[row][cols-1] =="O"):#last collumn
                dfs(row,cols-1)
        for col in range(cols):
            if(board[0][col] =="O"):#first row
                dfs(0,col)
            if(board[rows-1][col] =="O"):#last row
                dfs(rows-1,col)
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] =="O" and (i,j) not in seen):
                    board[i][j] = "X"