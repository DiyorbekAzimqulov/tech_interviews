class MinStack:

    def __init__(self):
        self.stack = []
        self.last_min = None
        self.cur_min = None

    def push(self, val: int) -> None:
        if self.cur_min is None:
            self.last_min = val
            self.cur_min = val
        elif val < self.cur_min:
            self.last_min = self.cur_min
            self.cur_min = val
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.cur_min:
            self.cur_min = self.last_min

    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cur_min
        

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-1))
print(minStack.getMin())
print(minStack.top())
print(minStack.pop())
print(minStack.getMin())