class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index,number in enumerate(numbers):
            need = target - number
            if need in seen:
                return [seen[need] + 1,index + 1]
            else:
                seen[number] = index