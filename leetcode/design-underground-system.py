class UndergroundSystem:

    def __init__(self):
        self.in_progress = {}
        self.completed = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        #customer has id :
        self.in_progress[id] = [stationName,t]
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.in_progress[id][0],stationName) in self.completed:
            self.completed[(self.in_progress[id][0],stationName)].append(t - int(self.in_progress[id][1]))
        else:
            self.completed[(self.in_progress[id][0],stationName)] = [t - int(self.in_progress[id][1])]
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sum_ = 0
        times = 0
        for time in self.completed[(startStation,endStation)]:
            sum_ += time
            times +=1
        return sum_ / times
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)