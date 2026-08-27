class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,num in enumerate(nums):
            need = target - num
            if need in seen:return index,seen[need]
            else: seen[num] = index