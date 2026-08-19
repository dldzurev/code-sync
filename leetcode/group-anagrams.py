class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}
        for item in strs:
            if "".join(sorted(item)) in anagram_dict:
                anagram_dict["".join(sorted(item))].append(item)
            else: anagram_dict["".join(sorted(item))] = [item]
        return list(anagram_dict.values())