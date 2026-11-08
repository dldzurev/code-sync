class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+","*","-","/"}
        ret = 1
        for tok in tokens:
            if tok in ops:
                if(stack):
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    if(tok == "+"):
                        stack.append(num1+num2)
                    elif(tok =="-"):
                        stack.append(num2 - num1)
                    elif(tok=="*"):
                        stack.append(num1*num2)
                    elif(tok=="/"):
                        stack.append(int(num2/num1))
                else:
                    return False
            else:
                stack.append(tok)
        return int(stack[0])