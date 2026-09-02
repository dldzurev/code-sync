class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        count = Counter(tasks)
        #freq,task
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        #freq,when run
        queue = deque()
        while queue or heap:
            while(queue and queue[0][1] <= t):
                heapq.heappush(heap,queue.popleft()[0])
            if heap:
                run = heapq.heappop(heap)
                run += 1
                if run < 0:
                    queue.append([run,t+n+1])

            t +=1
        return t