class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack.append(val)
            return
        if val<=self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)
        return
    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return  self.minstack[-1] if self.minstack else None
