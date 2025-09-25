class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = math.floor((left + right)/2)
        if(nums[0] == target):
            return 0
        if(len(nums) == 2 and nums[1] == target):
           return 1           

        while(left <= right):
            
            if(nums[mid] == target):
                return mid

            if(nums[mid] < target):
                left = mid+1
            if(nums[mid] > target):
                right = mid -1
            mid = math.floor((left + right) / 2) 
        return -1