class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows  = len(heights)
        cols = len(heights[0])
        min_heap = [[0,0,0]]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        while(min_heap):
            max_diff,row,col = heapq.heappop(min_heap)
            if((row,col) in seen): continue
            seen.add((row,col))
            if(row == rows-1 and col == cols-1): return max_diff

            for mod_row,mod_col in directions:
                new_row = row + mod_row
                new_col = col + mod_col
                if (new_row < 0 or new_row >= rows or
                    new_col < 0 or new_col >=cols or
                    (new_row,new_col) in seen):
                    continue
                new_diff = max(max_diff,abs(heights[row][col] - heights[new_row][new_col]))
                heapq.heappush(min_heap,[new_diff,new_row,new_col])