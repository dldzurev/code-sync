class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        left = 0
        right = len(p)-1
        freq_have = Counter(s[:len(p)-1])
        freq_need = Counter(p)
        ret = []
        while(right < len(s)):
            freq_have[s[right]] = 1 + freq_have.get(s[right],0)
            if(freq_have == freq_need):
                ret.append(left)
            if(freq_have[s[left]] == 1):
                del freq_have[s[left]]
            else:
                freq_have[s[left]] -= 1
            left +=1
            right +=1
       
        return ret