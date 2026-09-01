class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        curr_best = nums[0]
        for num in nums:
            curr_sum = max(curr_sum+num,num)
            curr_best = max(curr_sum,curr_best)

        return curr_best