class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_to_op = []
        for char in tokens:
            if char == "+":
                nums_to_op.append(nums_to_op.pop() + nums_to_op.pop())# 
            elif char == "-":
                nums_to_op.append(-nums_to_op.pop() + nums_to_op.pop())
            elif char == "*":
                nums_to_op.append(nums_to_op.pop() * nums_to_op.pop())
            elif char == "/":
                denominator = nums_to_op.pop()
                numerator = nums_to_op.pop()
                nums_to_op.append(int(numerator/denominator))
            else:
                nums_to_op.append(int(char))
        return nums_to_op[0]