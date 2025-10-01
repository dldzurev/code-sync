class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_ = 1
        nums.sort()
        for i in range (len(nums)):
            if(nums[i] == min_):
                min_ += 1
        return min_