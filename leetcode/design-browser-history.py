class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.forward_stack = []
        self.back_stack.append(self.curr)
        self.curr = url
        return

    def back(self, steps: int) -> str:
        if not self.back_stack:
            return self.curr
        _steps = min(steps-1,len(self.back_stack)-1)
        self.forward_stack.append(self.curr)
        for i in range(_steps):
            self.forward_stack.append(self.back_stack.pop())
        self.curr = self.back_stack.pop()
        return self.curr
    def forward(self, steps: int) -> str:
        if not self.forward_stack:
            return self.curr
        _steps = min(steps-1,len(self.forward_stack)-1)
        self.back_stack.append(self.curr)
        for i in range(_steps):
            self.back_stack.append(self.forward_stack.pop())
        self.curr = self.forward_stack.pop()
        return self.curr
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)