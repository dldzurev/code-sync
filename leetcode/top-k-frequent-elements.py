class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+ count.get(num,0) 
            heap = []
        for c in count:
            heapq.heappush(heap,[-count[c],c])
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret