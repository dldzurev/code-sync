class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        arrows = len(points)
        prev = points[0]
        for i in range(1,len(points)):
            point = points[i]
            _,p_end = prev
            start,end = point
            if(start <= p_end):
                prev = [start,min(end,p_end)]
                arrows -=1
            else:
                prev = point
        return arrows