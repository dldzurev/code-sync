class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ret  = len(nums)+1
        left = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while(curr_sum >= target):
                ret  = min(ret, r - left + 1)
                curr_sum -= nums[left]
                left +=1
        if(ret == len(nums)+1):
            return 0
        return ret