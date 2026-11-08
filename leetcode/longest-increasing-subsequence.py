class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            contender = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    contender = max(contender,dp[j])
            dp[i] = max(contender+1,dp[i])
        return max(dp)