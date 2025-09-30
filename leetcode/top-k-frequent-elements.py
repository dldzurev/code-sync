class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        order = []
        freq_arr = []

        y=1
        freq = 0
        for i in range(len(nums)):
            #print("i")
            if(nums[i] == nums[i-1 + y]):
                y = 0
                freq += 1

            else:
                #print(freq_arr)
                freq_arr.append(freq)
                order.append(nums[i-1])
                freq = 1
        order.append(nums[i])
        freq_arr.append(freq)
        ret = []
        for i in range(k):
            r = max(freq_arr)
            f = freq_arr.index(r)
            ret.append(order[f])            
            freq_arr[f] = 0
        return ret