class NumberContainers:
    def __init__(self):
        self.my_dict = {}
        self.arr = {}
        
    def change(self, index: int, number: int) -> None:
        self.arr[index] = number
        if number in self.my_dict:
            heapq.heappush(self.my_dict[number],index)
        else:
            self.my_dict[number] = [index]

    def find(self, number: int) -> int:
        if(number in self.my_dict):
            while(len(self.my_dict[number])>0):
                if self.arr[self.my_dict[number][0]] == number:
                    return self.my_dict[number][0]
                heapq.heappop(self.my_dict[number])  
        return -1