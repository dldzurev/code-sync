class MinStack:

    def __init__(self):
        # init
        self.stack = []
        self.min_heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_heap:
            push = min(val,self.min_heap[0])
        else:
            push = val
        heapq.heappush(self.min_heap,push)
        # push val onto stack
    def pop(self) -> None:
        # remove element at top of stack
        self.stack.pop()
        heapq.heappop(self.min_heap)

    def top(self) -> int:
        #get top element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]
        # min element in stack