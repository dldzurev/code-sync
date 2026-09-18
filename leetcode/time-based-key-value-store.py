class TimeMap:

    def __init__(self):
        self.my_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_dict:
            self.my_dict[key].append([timestamp,value])
        else:
            self.my_dict[key] = [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.my_dict and len(self.my_dict[key])>0:
            for i in range(len(self.my_dict[key])-1,-1,-1):
                if self.my_dict[key][i][0] <= timestamp:
                    return self.my_dict[key][i][1]
                
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)