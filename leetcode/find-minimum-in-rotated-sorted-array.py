class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right= 0, len(nums)-1
        if(nums[-1] > nums[0]):
            return nums[0]
        curr_min = nums[0]
        while(left<=right):            
            mid = (left + right)//2
            curr_min = min(curr_min,nums[mid])
            if(nums[mid] > nums[right]):
                left = mid+1
            else:
                right = mid-1
        return curr_min