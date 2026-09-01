class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes={0:1}
        curr_sum = 0
        result = 0
        for index,num in enumerate(nums):
            curr_sum += num
            diff = curr_sum - k
            result += prefixes.get(diff,0)
            prefixes[curr_sum] = 1 + prefixes.get(curr_sum,0) 
        return result