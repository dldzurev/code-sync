class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = []
        seen  = {} # key = val, val = index
        for i in range(len(nums)):
            need = target - nums[i] 
            if need in seen:
                op.extend((i,seen[need]))
            seen[nums[i]] = i

        return op