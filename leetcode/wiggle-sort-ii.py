class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,5,1,1,6,4]
        [1,1,1,4,5,6]
        [6,5,4,1,1,1]
        [1,6,1,5,1,4]
        """
        nums.sort()

        mid = (len(nums) + 1) // 2
        
        small = nums[:mid]
        large = nums[mid:]

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = small.pop()
            else:
                nums[i] = large.pop()