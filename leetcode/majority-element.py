import math
class Solution(object):
    def majorityElement(self, nums):
        target = (len(nums)/2)+1
        nums.sort()
        appear = 1
        i = 0
        while(appear < target):
            if( (i > 0) and (nums[i] == nums[i-1])):
                appear += 1
                i+=1
            else:
                appear = 1
                i+=1
                

 
        return nums[i-1]

        """
        :type nums: List[int]
        :rtype: int
        """