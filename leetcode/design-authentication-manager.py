class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.count = 0
        self.map = {}
        self.heap = []
    def generate(self, tokenId: str, currentTime: int) -> None:

        while( self.heap and self.heap[0][0] <= currentTime):
            if(self.heap[0][0] != self.map[self.heap[0][1]]):
                heapq.heappop(self.heap)
                continue
            time , id_ = heapq.heappop(self.heap)
            self.count -= 1
            del self.map[id_]
        heapq.heappush(self.heap, [self.timeToLive + currentTime, tokenId])
        self.map[tokenId] = currentTime + self.timeToLive
        self.count += 1
        return
    def renew(self, tokenId: str, currentTime: int) -> None:
        while( self.heap and self.heap[0][0] <= currentTime):
            if(self.heap[0][0] != self.map[self.heap[0][1]]):
                heapq.heappop(self.heap)
                continue
            time , id_ = heapq.heappop(self.heap)
            self.count -= 1
            del self.map[id_]
        if tokenId in self.map:
            self.map[tokenId] = currentTime + self.timeToLive
            heapq.heappush(self.heap, [currentTime + self.timeToLive, tokenId])
        return
    def countUnexpiredTokens(self, currentTime: int) -> int:
        while(self.heap and self.heap[0][0] <= currentTime):
            if(self.heap[0][0] != self.map[self.heap[0][1]]):
                heapq.heappop(self.heap)
                continue
            time , id_ = heapq.heappop(self.heap)
            self.count -= 1
            del self.map[id_]
        return self.count