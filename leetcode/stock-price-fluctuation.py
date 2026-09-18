class StockPrice:
    def __init__(self):
        self.price_dict = {}
        self.min_price = []
        self.max_price = []
        self.last_time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.last_time = max(self.last_time,timestamp)
        self.price_dict[timestamp] = price
        heapq.heappush(self.max_price,[-price,timestamp])
        heapq.heappush(self.min_price,[price,timestamp])

    def current(self) -> int:
        return self.price_dict[self.last_time]
        
    def maximum(self) -> int:
        while(self.max_price):
            p , t = self.max_price[0]
            p = p*(-1)
            if p == self.price_dict[t]:
                return p
            heapq.heappop(self.max_price)
        return

    def minimum(self) -> int:
        while(self.min_price):
            p , t = self.min_price[0]
            if p == self.price_dict[t]:
                return p
            heapq.heappop(self.min_price)
        return