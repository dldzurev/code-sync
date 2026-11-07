class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = -1
        curr_sum = 0
        best = len(nums) + 1
        while(right < len(nums)):  
            if(curr_sum >= target and (right-left + 1) < best):
                best = right - left + 1
            if(left < right and curr_sum > target):
                curr_sum -= nums[left]
                left += 1
            else:
                right +=1
                if(right<len(nums)):
                    curr_sum += nums[right]

        if(best == len(nums) +1):
            return 0
        return best