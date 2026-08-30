class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        #s1 = ccc
        #s2 = cbac
        while(start <= (len(s2) - len(s1))):# 0 <= (4-3) -> 0<=1
            permutations = Counter(s1) #{ccc}
            end = start
            while(s2[end] in permutations):
                if permutations[s2[end]] == 1:
                    permutations.pop(s2[end]) 
                else:
                    permutations[s2[end]] -=1
                end+=1
                if(len(permutations) == 0):
                    return True
            start+=1    
        return False