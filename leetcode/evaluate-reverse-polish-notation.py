class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #["4","13","5","/","+"]
        ops = {"+","-","*","/"}
        stack = []#[4,13,5]
        for token in tokens:#/

            if token in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if (token == "-"):
                    print(num2,"-",num1)
                    stack.append(num2 - num1)
                elif (token == "+"):
                    print(num1,"+",num2)
                    stack.append(num1 + num2)
                elif (token == "*"):
                    print(num1,"*",num2)
                    stack.append(num1 * num2)
                else:
                    print(num2,"/",num1)
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        return stack[0]