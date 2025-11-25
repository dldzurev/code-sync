class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        holds = True
    
        it = 0
        if(len(strs) == 1):
            return strs[0]
        while(holds and it < len(strs[0])):
            curr = strs[0][it]
            for i in range(1,len(strs)):
                if(len(strs[i]) <= it or strs[i][it] != curr):
                    holds = False
     
            if(holds):
                it+=1
        return strs[0][:it]