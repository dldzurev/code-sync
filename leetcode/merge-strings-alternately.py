class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i,y in zip(word1,word2):
            res.append(i)
            res.append(y)
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])
        return "".join(res)