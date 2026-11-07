class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        queue = deque()
        left = 0
        right = 0
        seen = set()
        max_ = 1

        while(right < len(s)):
            while(s[right] in seen):
                left +=1
                popped = queue.popleft()
                seen.remove(popped)
            else:
                seen.add(s[right])
                queue.append(s[right])
                if(len(seen) > max_):
                    max_ = len(seen)
                right +=1
        return max_