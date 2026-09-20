class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen =deque()#p
        seen_set = set()
        curr_max = 0#2
        tot_max = 0#2
        for string in s:#w
            while(string in seen_set):
                seen_set.discard(seen.popleft())
                curr_max -=1
            seen.append(string)
            seen_set.add(string)
            curr_max+=1
            tot_max = max(tot_max,curr_max)
        return tot_max