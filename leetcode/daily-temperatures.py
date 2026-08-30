class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures) 
        temp_stack = []
        for index, temp in enumerate(temperatures):
            while(temp_stack and temp > temp_stack[-1][1]):
                index2 = temp_stack.pop()[0]
                answer[index2] = index-index2
            temp_stack.append([index,temp])
        return answer