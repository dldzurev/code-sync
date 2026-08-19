class Solution:
    def isValid(self, s: str) -> bool:
        my_hash = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for char in s:
            if(char in my_hash):
                if(not stack):
                    return False
                if(stack[-1] != my_hash[char]):
                    return False
                stack.pop()
            else:
                stack.append(char)

  
        return len(stack) == 0