class MinStack:

    def __init__(self):
        self.stack = []
        
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            top_val = self.stack[-1][1]
            if val < self.stack[-1][1]:
                self.stack.append((val, val))
            else:
                self.stack.append((val, top_val))

        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
