class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if(nums[i] not in seen):
                seen[nums[i]]= nums.count(nums[i])
        ret = []
        for s in range (k):
                top_key = max(seen, key=seen.get)  
                ret.append(top_key)                
                del seen[top_key]    
        return ret