class Solution:
    def isValid(self, s: str) -> bool:
        #last item in stack2 must be the oposit of last of stack1 or open bracket
        bracket_map = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        popped_stack = []
        
        for char in s:
            if char in bracket_map:
                #its a closing bracket
                if not popped_stack:
                    return False

                x = popped_stack.pop()
                if not(x == bracket_map[char]):
                    return False
            else:
                popped_stack.append(char)
        if len(popped_stack) == 0:
            return True
        else:
            return False