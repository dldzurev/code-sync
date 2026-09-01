class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reaches_pacific = set()
        reaches_atlantic = set()
        cols = len(heights[0])
        rows = len(heights)
        def dfs(row,col,min_height,seen):
            if (row<0 or row == rows or
                col<0 or col == cols or
                (row,col) in seen or
                heights[row][col] < min_height): return
            seen.add((row,col))
            dfs(row + 1,col,heights[row][col],seen)
            dfs(row - 1,col,heights[row][col],seen)
            dfs(row,col + 1,heights[row][col],seen)
            dfs(row,col - 1,heights[row][col],seen)
        for col in range(cols):
            dfs(0,col,0,reaches_pacific)
            dfs(rows - 1,col,0,reaches_atlantic)
        for row in range(rows):
            dfs(row,0,0,reaches_pacific)
            dfs(row,cols - 1,0,reaches_atlantic)
        return list(reaches_pacific & reaches_atlantic)