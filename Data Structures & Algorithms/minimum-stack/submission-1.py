from collections import deque

class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minVal = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVal:
            self.minVal.append(val)
        elif self.minVal[-1] >= val:
            self.minVal.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.getMin() == popped:
            self.minVal.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]     
