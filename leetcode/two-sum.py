class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for x in nums:
            need = target - x
            if need in seen: return i, seen[need]
            else: seen[x] = i
            i += 1