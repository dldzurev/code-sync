class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        completed = set()
        indegree = [0]*numCourses
        pre_to_cor = {i:[] for i in range(numCourses)}
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            indegree[course] += 1
            pre_to_cor[prereq].append(course)
        queue = deque()
        for cour,indeg in enumerate(indegree):
            if(indeg == 0):
                queue.append(cour)
        while(queue):
            popped = queue.popleft()
            res.append(popped)
            for cor in pre_to_cor[popped]:
                indegree[cor] -= 1
                if(indegree[cor] == 0):
                    queue.append(cor)
            del pre_to_cor[popped]
        if len(pre_to_cor) != 0: return []
        return res