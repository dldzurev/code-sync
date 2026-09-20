class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()
        for interval in intervals:
            start,end = interval
            if (ret and ret[-1][1] >= start):
                ret[-1][1] = max(ret[-1][1],end)
            else:
                ret.append([start,end])
        return ret