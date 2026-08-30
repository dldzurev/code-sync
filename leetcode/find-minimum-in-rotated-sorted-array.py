class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[-1] > nums[0]:
            return nums[0]

        while left < right:              

            mid = left + (right-left)//2

            if mid < len(nums) - 1 and nums[mid+1] < nums[mid]:
                return nums[mid+1]

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid                

        return nums[left]