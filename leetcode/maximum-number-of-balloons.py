class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #balloon
        seen = {
            "b":0,
            "a":0,
            "l":0, #need 2
            "o":0, #need 2
            "n":0
        }
        for i in range(len(text)):
            if(text[i] in seen):
                seen[text[i]] +=1
        seen["l"] = seen["l"]//2
        seen["o"] = seen["o"]//2
        times = min(seen.values())

        return times