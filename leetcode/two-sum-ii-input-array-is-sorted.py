class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        need = {}
        for i in range (len(numbers)):
            need_ = target - numbers[i] 
            if(need_ in need):
                return need[need_] + 1, i + 1
            else:
                need[numbers[i]] = i