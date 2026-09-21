class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows-1
        while(top <= bottom):
            mid_row = (top+bottom)//2
            if(matrix[mid_row][-1] < target):
                top = mid_row+1
            elif(matrix[mid_row][0] > target):
                bottom = mid_row-1
            else:
                break
        if(top > bottom):
            return False
        row = (top + bottom )//2
        left = 0
        right = cols
        while(left <=right):
            mid = (left+right)//2
            if(target == matrix[row][mid]):
                return True
            if(matrix[row][mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return False