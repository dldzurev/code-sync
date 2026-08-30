class Solution:
    def isValid(self, s: str) -> bool:
        #([])
        bracket_map = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        popped_stack = []#([
        for bracket in s:#]

            if bracket in bracket_map and popped_stack:
                if  bracket_map[bracket] != popped_stack[-1]:
                    return False
                popped_stack.pop()
            else:
                popped_stack.append(bracket)
                
            
        return (len(popped_stack) == 0)