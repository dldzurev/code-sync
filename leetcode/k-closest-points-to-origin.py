class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            print(distance)
            heapq.heappush(heap,(distance,point))
            print()
        return [heapq.heappop(heap)[1] for i in range(k)]