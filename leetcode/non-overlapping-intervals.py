class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        remove=0
        res=[]
        for interval in intervals:
            start,end = interval
            if res:
                prev_start,prev_end = res[-1]
                if start < prev_end:
                    res[-1][1] = min(end,prev_end)
                    remove+=1
                    continue
            res.append([start,end])
        return remove