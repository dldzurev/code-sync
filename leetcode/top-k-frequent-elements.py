class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        res = []
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for n,c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1 ,-1,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res