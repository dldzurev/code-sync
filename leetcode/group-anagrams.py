class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            ret[key].append(item)     
        return list(ret.values())