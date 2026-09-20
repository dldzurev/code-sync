class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heap.append([x*x+y*y,[x,y]])
        heapq.heapify(heap)
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret