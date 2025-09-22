class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurences = 0
        i = len(nums) - 1

        while(i >= 0):
            if(nums[i] == val ):
                occurences += 1
                nums[i] = nums[len(nums) - occurences]
                

            i = i - 1
        return len(nums) - occurences