class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target -> index
        targ_map = {}
        for index,num in enumerate(nums):
            targ = target - num
            if(targ in targ_map):
                return [targ_map[targ],index]
            targ_map[num] = index