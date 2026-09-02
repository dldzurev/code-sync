class TimeMap:

    def __init__(self):
        self.key_to_vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_to_vals:
            self.key_to_vals[key].append([timestamp,value])
        else:
            self.key_to_vals[key] = [[timestamp,value]]
    #1 3 5 7 9
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_vals: return ""
        search_list = self.key_to_vals[key]
        if(search_list[0][0] > timestamp): return ""
        left = 0
        right = len(search_list) - 1
        result = ""
        while(left <= right):
            mid = left + (right - left)//2
            if(search_list[mid][0] == timestamp):
                return search_list[mid][1]
            if(search_list[mid][0] > timestamp):
                right = mid-1
            else:
                result = search_list[mid][1]
                left = mid+1
        return result

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)