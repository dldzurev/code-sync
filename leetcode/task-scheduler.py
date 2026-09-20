class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0 
        n=n+1
        remaining = {}
        heap = []
        wait = deque()#freq,cooldown
        for task in tasks:
            remaining[task] = 1 + remaining.get(task,0)
        print(remaining)
        for task in remaining:
            heapq.heappush(heap,[-remaining[task],0])#freq,cooldown
        while(heap or wait):
            while wait and wait[0][1] <= cycles:
                freq,cool = wait.popleft()
                heapq.heappush(heap,[-(freq),0])
            if(heap):
                freq,cool = heapq.heappop(heap)
                freq = -freq
                if freq > 1:
                    wait.append([freq-1,cycles+n])

                    
            cycles+=1
        return cycles