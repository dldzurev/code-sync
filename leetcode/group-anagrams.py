class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for string in strs:
            base = "".join(sorted(string))
            if(base in my_dict):
                my_dict[base].append(string)
            else:
                my_dict[base]=[string]
        if(my_dict):
            return list(my_dict.values())
        else:
            return list("")