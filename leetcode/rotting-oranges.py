class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        num_ripe = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    rotten.append([i,j])#row,col
                elif(grid[i][j] == 1):
                    num_ripe +=1
        seen = set()
        q = deque()
        print()
        while(rotten):
            for i in range(len(rotten)):
                row,col = rotten.popleft()
                if((row,col) not in seen):
                    seen.add((row,col))
                    if((row,col+1) not in seen and col+1 < len(grid[0]) and grid[row][col+1] == 1):
                        grid[row][col+1] = 2
                        num_ripe-=1
                        q.append([row,col+1])
                    if((row,col-1) not in seen and col-1 >= 0 and grid[row][col-1] == 1):
                        grid[row][col-1] = 2
                        num_ripe-=1
                        q.append([row,col-1])
                    if((row+1,col) not in seen and row+1 < len(grid) and grid[row+1][col] == 1):
                        grid[row+1][col] = 2
                        num_ripe-=1
                        q.append([row+1,col])
                    if((row-1,col) not in seen and row-1 >= 0 and grid[row-1][col] == 1):
                        grid[row-1][col] = 2
                        num_ripe-=1
                        q.append([row-1,col])
            if q: time += 1
            rotten = q
            q = deque()
        if(num_ripe > 0):
            print(time)
            return -1
        else:
            return time