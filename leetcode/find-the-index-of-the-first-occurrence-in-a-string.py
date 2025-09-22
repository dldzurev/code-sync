class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = False
        index = 0

        needle_len = len(needle) 
        for y in range (len(haystack) - len(needle) + 1):
            if haystack[y] == needle[0]:
                i=0
                while( i < needle_len and haystack[y + i] == needle[i] ):
                    
                    i = i + 1
                if(i == needle_len):
                        return y
        return -1