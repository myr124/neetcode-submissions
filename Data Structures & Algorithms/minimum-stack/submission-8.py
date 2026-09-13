class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.min = val
            self.minList.append(self.min)

    def pop(self) -> None:
        if self.stack[-1] == self.minList[-1]:
            self.stack.pop()
            self.minList.pop()
            if self.minList:
                self.min = self.minList[-1]
            else:
                self.min = float("inf")
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[-1]

        
