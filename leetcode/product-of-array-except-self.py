class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for i,num in enumerate(nums):
            if(i == len(nums)-1):
                pass
            else:
                suffix[i+1] = suffix[i]*nums[i]
                prefix[-i-2] = prefix[-i-1]*nums[-i-1]
        res = []
        print(suffix)
        print(prefix)
        for suff,pre in zip(suffix,prefix):
            res.append(suff*pre)
        return res