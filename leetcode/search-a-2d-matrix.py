class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = 0
        m = len(matrix[0]) - 1#cols
        row = 0
        n = len(matrix) - 1# rows
        mid_row = 0
        while(row <= n):
            mid_row = row + (n-row)//2
            if(matrix[mid_row][0] <= target <= matrix[mid_row][m]):
                break
            elif(matrix[mid_row][0] > target):
                n= mid_row - 1
            else:
                row = mid_row + 1
        else: return False
        while(col <= m):
            mid_col = col + (m-col)//2
            if matrix[mid_row][mid_col] == target:
                return True
            elif(matrix[mid_row][mid_col] > target):
                m = mid_col - 1
            else:
                col = mid_col + 1
        return False