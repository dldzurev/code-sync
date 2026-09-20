class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        curr = 0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0)
            curr+=1
            while(curr - max(count.values()) > k):
                curr -=1
                count[s[left]] -=1
                left +=1
            res = max(res,curr)
        return res