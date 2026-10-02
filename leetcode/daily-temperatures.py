class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = deque()
        res = [0] * len(temperatures)
        for index,temp in enumerate(temperatures):
            while waiting and temp > waiting[-1][0]:
                _,day = waiting.pop()
                res[day] = index - day
            waiting.append([temp,index])
        return res