class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:]) #27
        print(right_sum)
        if(left_sum == right_sum ):
            return 0
        for i in range(1,len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            if(left_sum == right_sum):
                return i
        if(sum(nums[0:-1]) == 0):
            return 0
        return -1