class Solution:

    def calculate(self, s: str) -> int:
        def get_num(index):
            end_index = index
            while(end_index < len(s) and s[end_index] != " " and s[end_index] != "/" and s[end_index] != "*" and s[end_index] != "+" and s[end_index] != "-"):
                end_index += 1
            return end_index 

        if(len(s) == 1):
            return int(s)

        i = 0
        stack = []
        while(i < len(s)):
            char = s[i]
            if(char == " "):
                i += 1
                continue
            if(char == "*" or char == "/" or char == "+" or char == "-"):
                stack.append(char)
            else:
                end = get_num(i)
                num = int(s[i:end])
                stack.append(num)
                i = end - 1  
            i += 1

        stack_2 = [stack[0]]  

        for i in range(1, len(stack), 2):

            right = stack[i+1]

            if(stack[i] == "*"):
                left = stack_2.pop()
                stack_2.append(right * left)

            elif(stack[i] == "/"):
                left = stack_2.pop()
                stack_2.append(int(left / right))  

            else:
                stack_2.append(stack[i])
                stack_2.append(right) 

        res = stack_2[0]

        for i in range(1, len(stack_2), 2):
            if(stack_2[i] == "+"):
                res += stack_2[i+1]
            else:
                res -= stack_2[i+1]

        return res