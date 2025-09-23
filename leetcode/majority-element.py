class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        curr_max = 0
        curr_max_element = nums[0]
        curr_candidate = nums[0]
        curr_count = 1
        
        for i in range(len(nums)):
            if(i > 0):
                if(nums[i] == curr_candidate):
                    curr_count += 1
                    if(curr_count > curr_max):
                        curr_max_element = nums[i]
                        curr_max = curr_count
                else:
                    curr_candidate = nums[i]
                    curr_count = 1
        return curr_max_element