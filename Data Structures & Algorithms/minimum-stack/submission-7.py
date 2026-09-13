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
        print("min" + str(self.minList))
        print("stack" + str(self.stack))


    def pop(self) -> None:
        if self.stack[len(self.stack)-1] == self.minList[len(self.minList)-1]:
            self.stack.pop()
            self.minList.pop()
            print(len(self.minList))
            if self.minList:
                self.min = self.minList[len(self.minList)-1]
            else:
                self.min = float("inf")
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if self.minList:
            print(self.minList[len(self.minList)-1])
            return self.minList[len(self.minList)-1]
        else:
            return None
        
