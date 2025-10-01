class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1 = 0
        for l2 in range(len(nums)):
            if nums[l2] != 0:
                temp = nums[l1]
                nums[l1] = nums[l2]
                nums[l2] = temp            
                l1+=1