class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()
        def find_connections(grid,row,col,seen):
            if(grid[row][col] == "0"):
                return
            seen.add((row,col))
            if(not((row+1,col) in seen) and row + 1 < len(grid)):
                find_connections(grid,row+1,col,seen)
            if(not((row-1,col) in seen) and row - 1 >= 0):   
                find_connections(grid,row-1,col,seen)
            if(not((row,col+1) in seen) and col + 1 < len(grid[0])):
                find_connections(grid,row,col+1,seen)
            if (not((row,col-1) in seen) and col - 1 >= 0):
                find_connections(grid,row,col-1,seen)
            return
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not((row,col) in seen):
                    count +=1
                    find_connections(grid, row, col,seen)
        return count