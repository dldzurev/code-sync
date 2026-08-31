class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #1 <= k <= len(nums). 2
        #| | |
        #5,1,3
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid  = left + (right-left)//2
            if(nums[mid] == target):
                return mid
            if(nums[left] <= nums[mid]): #left sorted mins element is at left
                if (nums[left] <= target < nums[mid]):
                    right = mid -1
                else:
                    left = mid + 1

            elif(nums[right] >= nums[mid]):# right sorted min element is at mid
                if(nums[right] >= target > nums[mid]):
                    left = mid+1
                else:
                    right = mid - 1
        return -1