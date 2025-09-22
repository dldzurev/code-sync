class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        max_occurrence = 0
        seen = set()

        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num in seen:
                continue
            seen.add(curr_num)

            curr_freq = 0
            for j in range(len(nums)):
                if nums[j] == curr_num:
                    curr_freq += 1

            if curr_freq > max_freq:
                max_freq = curr_freq
                max_occurrence = 1
            elif curr_freq == max_freq:
                max_occurrence += 1

        return max_freq * max_occurrence