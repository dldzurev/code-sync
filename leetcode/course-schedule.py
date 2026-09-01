class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        completed = set()
        pre_cor = {i:[] for i in range(numCourses)}
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            pre_cor[prereq].append(course)
            indegree[course] += 1
        queue = deque()
        for course, indeg in enumerate(indegree):
            if (indeg == 0 and course not in completed):
                completed.add(course)
                queue.append(course)
        while(queue):
            popped = queue.popleft()
            for cor in pre_cor[popped]:
                indegree[cor] -= 1
                if (indegree[cor] == 0 and cor not in completed):
                    completed.add(cor)
                    queue.append(cor)
            del pre_cor[popped]
        return len(pre_cor) == 0