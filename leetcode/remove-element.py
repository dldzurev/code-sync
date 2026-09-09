class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = len(nums) -1 #3
        right  = left #3
        while(left >= 0):#3>0
            if nums[left] == val:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
            left -= 1
        return right+1