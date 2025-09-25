class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range (len(nums)):
            curr = nums[i]
            need = target - curr

            if need in seen:
                return [seen[need],i]
            seen[curr] = i