class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        x = 0
        for i in range(len(nums)):
            if(nums[i] in seen):
                return True
            else:
                seen[nums[i]] = nums[i]
                x += 1
        return False