class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        while(left <= right):
            holds = True
            left_as_str = str(left)
            for i in range(len(left_as_str)):
                if(int(left_as_str[i]) == 0):
                    holds = False

                elif(left % int(left_as_str[i]) !=0):
                    holds = False
            if(holds):
                ret.append(left)
            left+=1
        return ret