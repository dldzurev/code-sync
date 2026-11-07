class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while(stones):
            if(len(stones) == 1):
                return -stones[0]
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)
            if(stone_1 == stone_2):
                continue
            elif(stone_1 > stone_2):
                heapq.heappush(stones, -(stone_1 - stone_2))
            else:
                heapq.heappush(stones, -(stone_2 - stone_1))
        return 0