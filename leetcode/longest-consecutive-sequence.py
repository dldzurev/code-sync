class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        curr_count = 1
        if len(nums) == 0: return 0
        prev = nums[0]
        seq_freq = []
        heapq.heapify(seq_freq)
        for i in range(1,len(nums)):

            if ((nums[i] == prev+1 or nums[i] == prev-1)) :
                curr_count+=1
            elif(prev != nums[i]):
                heapq.heappush(seq_freq,-curr_count)
                curr_count = 1
            prev = nums[i]
        heapq.heappush(seq_freq,-curr_count)
        return -seq_freq[0]