class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        start, end = newInterval
        for i in range(len(intervals)):
            if intervals[i][1] < start:
                merged.append(intervals[i])
            elif end < intervals[i][0]:
                return merged + [[start, end]] + intervals[i:]
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
        merged.append([start, end])
        return merged