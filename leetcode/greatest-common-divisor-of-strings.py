class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1,len2 = len(str1),len(str2)
        def valid(l):
            if len1 % l or len2 % l:
                return False 
            f1,f2 = len1 // l , len2 // l
            if(f1* str1[0:l] == str1 and f2 * str1[0:l] == str2):
                return True
            return False

        for i in range(min(len1,len2),0,-1):
            if (valid(i)):
                return str1[0:i]
        return ""