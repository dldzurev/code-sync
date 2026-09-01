class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh_oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.append([row,col])
                elif grid[row][col] == 1:
                    fresh_oranges +=1
        if not fresh_oranges: return 0
        time = 0 
        while rotten: 
            time+=1
            to_rot = []
            while(rotten):
                row,col = rotten.pop()
                if(row + 1 < len(grid) and grid[row+1][col] == 1):
                    to_rot.append([row+1,col])
                    grid[row+1][col] = 2
                    fresh_oranges -=1
                if(row - 1 >= 0 and grid[row-1][col] == 1):
                    to_rot.append([row-1,col])
                    grid[row-1][col] = 2
                    fresh_oranges -=1
                if(col + 1 < len(grid[0]) and grid[row][col+1] == 1):
                    to_rot.append([row,col+1])
                    grid[row][col+1]= 2
                    fresh_oranges -=1
                if(col - 1 >= 0 and grid[row][col-1] == 1):
                    to_rot.append([row,col-1])
                    grid[row][col-1] = 2
                    fresh_oranges -=1
            rotten.extend(to_rot)
        if fresh_oranges > 0: return -1
        return time-1