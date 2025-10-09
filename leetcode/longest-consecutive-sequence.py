class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_max = 1
        curr_count = 1
        nums.sort()
        if(len(nums) == 0):
            return 0
        for i in range(1,len(nums),1):
            if (nums[i-1] + 1) == nums[i] :
                curr_count += 1
                if curr_count > curr_max: curr_max = curr_count
            elif nums[i-1] == nums[i]:
                continue
            else:
                curr_count = 1
            
            
        return curr_max