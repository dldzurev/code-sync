class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     #   ABAB
     #k = 2
        char_freq = defaultdict(int)
        start = 0
        end = 0
        max_ = 0
        while(end < len(s)):
            size = end-start + 1 
            char_freq[s[end]]+=1
            while(size - max(char_freq.values()) > k):
                char_freq[s[start]] -=1
                start +=1
                size -=1
            else:
                end +=1
            max_ = max(max_,size)
        return max_