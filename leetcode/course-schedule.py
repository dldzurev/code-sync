class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_ = {i:[] for i in range (numCourses)}
        for crs,preq in prerequisites:
            map_[crs].append(preq)
        seen = set()
        def dfs(crs):
            if(crs in seen):
                return False
            if(map_[crs] == []):
                return True
            seen.add(crs)
            for x in map_[crs]:
                if not dfs(x):
                    return False
            map_[crs] = []
            seen.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                
                return False
        return True