class Solution(object):
    def twoSum(self, nums, target):
        x=1
        
        while(x < (len(nums))):
            y=0
            while(y < x):
                if((nums[x] + nums[y]) == target):
                    return x,y
                y+=1
            x+=1