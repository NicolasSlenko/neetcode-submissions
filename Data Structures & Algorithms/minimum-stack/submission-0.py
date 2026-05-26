class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minVal.append(val)
        else:
            oldMin =  self.minVal[-1]
            if val < oldMin:
                 self.minVal.append(val)
            else:
                 self.minVal.append(oldMin)
            self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minVal.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        
