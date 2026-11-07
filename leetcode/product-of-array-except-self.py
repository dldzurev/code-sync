class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[-i -1] = suffix[-i] * nums[-i]
        res = []
        print(prefix)
        print(suffix)
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        return res