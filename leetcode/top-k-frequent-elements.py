class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = {}
        for num in nums:
            occurence[num] = occurence.get(num,0) + 1
        heap = []
        for key_ , val_ in occurence.items():
            heapq.heappush(heap,[-val_,key_])
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret