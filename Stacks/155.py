class MinStack:
    # TIME: O(1)
    # SPACE: O(n)
    def __init__(self):
        self.stk = []
        self.min_stk = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()