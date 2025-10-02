class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        i, p = 0, k
        window = sum(nums[i:p])
        curr_max = window / k             

        while p < len(nums):
            window = window - nums[i] + nums[p]
            curr_max = max(curr_max, window / k)
            i += 1
            p += 1

        return curr_max