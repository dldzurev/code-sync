class Solution:
    def reorganizeString(self, s: str) -> str:
        hash_ = {}
        num_chars = len(s)
        
        for i in range(len(s)):
            if(s[i] in hash_):
                hash_[s[i]] +=1
            else:
                hash_[s[i]] = 1
        if(max(hash_.values()) > math.ceil(num_chars/2)):
            return ""
        else:
            ret = ""
            hold_val = 0
            hold_key = ""
            for i in range(len(s)):
                max_ = max(hash_, key = hash_.get)
                ret = ret + (max_)
                #restore
                hash_[hold_key] = hold_val
                #mute
                hold_key = max_
                hold_val = hash_[max_] -1
                hash_[max_] = 0

        return ret