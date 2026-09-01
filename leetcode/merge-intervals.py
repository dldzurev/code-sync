class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()
        res.append(intervals[0])
        for i in range(len(intervals)):
            prev = res[-1]
            if prev[1] >= intervals[i][0]:
                res[-1] = [prev[0],max(prev[1],intervals[i][1])]
            else:
                res.append(intervals[i])
            
        return res