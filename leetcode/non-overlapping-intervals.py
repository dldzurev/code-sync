class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        queue = []
        for i in range(len(intervals)):
            if(queue):

                last_start,last_end = queue[-1]
                if(intervals[i][0] < last_end and last_end > intervals[i][1]):
                    queue.pop()
                    queue.append([intervals[i][0],intervals[i][1]])
                elif intervals[i][0] >= last_end:
                    queue.append(intervals[i])

            else:
                queue.append(intervals[i])
        return len(intervals) - len(queue)